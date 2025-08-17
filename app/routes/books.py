from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database, auth

router = APIRouter(prefix="/books",tags=["books"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create",response_model=schemas.BookOut)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db), user: models.User = Depends(auth.get_current_user)):
    db_book = models.Book(**book.dict(), owner_id= user.id)
    db_book.update_status()
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get("/", response_model=list[schemas.BookOut])
def get_books(db: Session = Depends(get_db),user: models.User = Depends(auth.get_current_user)):
    return db.query(models.Book).filter(models.Book.owner_id == user.id).all()

@router.get("/{book_id}",response_model=schemas.BookOut)
def get_book(book_id: int, db: Session = Depends(get_db), user: models.User = Depends(auth.get_current_user)):
    book = db.query(models.Book).filter(models.Book.id == book_id, models.Book.owner_id == user.id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=schemas.BookOut)
def update_book(book_id: int, update: schemas.BookUpdate, db: Session = Depends(get_db), user: models.User = Depends(auth.get_current_user)):
    book = db.query(models.Book).filter(models.Book.id == book_id, models.Book.owner_id == user.id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if update.pages_read < 0 or update.pages_read > book.total_pages:
        raise HTTPException(status_code=400, detail="Invalid pages count")
    book.pages_read = update.pages_read
    book.update_status()
    db.commit()
    db.refresh(book)
    return book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db), user: models.User = Depends(auth.get_current_user)):
    book = db.query(models.Book).filter(models.Book.id == book_id, models.Book.owner_id == user.id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"detail":"Book deleted"}