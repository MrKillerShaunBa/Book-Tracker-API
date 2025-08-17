from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    author: str
    total_pages: int
    pages_read: int = 0

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    pages_read: int

class BookOut(BookBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True

class PasswordUpdate(BaseModel):
    old_password:str
    new_password:str