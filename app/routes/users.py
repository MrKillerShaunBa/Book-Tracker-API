from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from .. import models, schemas, database, auth,utils

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/me", response_model=schemas.UserOut,summary="Get current user",description="Retrieve the details of the currently authenticated user.")
def get_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user

@router.get("/me/stats",summary="Get reading statistics",description="Retrieve statistics about the user's reading progress.")
def my_reading_stats(db: Session = Depends(get_db),current_user: models.User = Depends(auth.get_current_user)):
    base_query = db.query(models.Book).filter(models.Book.owner_id == current_user.id)
    total_books = base_query.count()
    completed = base_query.filter(models.Book.status == "Completed").count()
    in_progress = base_query.filter(models.Book.status == "In Progress").count()
    not_started = base_query.filter(models.Book.status == "Not Started").count()

    total_pages = (db.query(func.sum(models.Book.total_pages).filter(models.Book.owner_id == current_user.id)).scalar() or 0)
    pages_read = (db.query(func.sum(models.Book.pages_read).filter(models.Book.owner_id == current_user.id)).scalar() or 0)
    completion_rate = (pages_read / total_pages * 100) if total_pages > 0 else 0.0
    return {
        "total_books": total_books,
        "completed": completed,
        "in_progress": in_progress,
        "not_started": not_started,
        "total_pages": total_pages,
        "pages_read": pages_read,
        "completion_rate": completion_rate
    }
