from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    books = relationship("Book", back_populates="owner")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    total_pages = Column(Integer)
    pages_read = Column(Integer, default=0)
    status = Column(String, default="Not Started")
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User",back_populates="books")
    
    def update_status(self):
        if self.pages_read == 0:
            self.status = "Not Started"
        elif self.pages_read < self.total_pages:
            self.status = "In Progress"
        else:
            self.status = "Completed"