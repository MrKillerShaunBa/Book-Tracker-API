from fastapi import FastAPI
from . import models, database
from .routes import books,users
from . import auth

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Book Tracker API", description="Track your reading progress. Add your books, their total number of pages and keep a track of how much you have completed.")

app.include_router(auth.router)
app.include_router(books.router)
app.include_router(users.router)