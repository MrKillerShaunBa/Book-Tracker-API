from pydantic import BaseModel,Field

class UserCreate(BaseModel):
    username: str = Field(..., example="username")
    password: str = Field(..., example="password")

class UserOut(BaseModel):
    id: int
    username: str = Field(..., example="username")
    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str = Field(..., example="Book title")
    author: str = Field(..., example="Book author")
    total_pages: int = Field(..., example=0)
    pages_read: int = Field(..., example=0)

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    pages_read: int

class BookOut(BookBase):
    id: int
    owner_id: int
    status: str = Field(..., example="Not Started/In Progress/Completed")
    class Config:
        orm_mode = True

class ReadingStatsResponse(BaseModel):
    total_books: int = Field(..., example=10)
    completed: int = Field(..., example=5)
    in_progress: int = Field(..., example=3)
    not_started: int = Field(..., example=2)
    total_pages: int = Field(..., example=300)
    pages_read: int = Field(..., example=150)
    completion_rate: float = Field(..., example=50.0)

class BookStatus(BookBase):
    status: str = Field(..., example="Not Started/In Progress/Completed")

class TokenOut(BaseModel):
    access_token: str = Field(..., example="access_token")
    token_type: str = "bearer"