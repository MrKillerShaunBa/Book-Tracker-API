# Book Tracker API

This is FastAPI based Book Tracker which allows you to save the progress (number of pages read) of the books you are reading. It helps to keep a track of the books you have finished, are currently reading and have not started. My motivation to build this was that I have a large library of books at home and have a hard time remembering where I left a particular book when I didn't use a bookmark. I plan to add a front-end to this in the future.

## Hosted API Docs

You can see the hosted Swagger docs [https://book-tracker-api-0ejh.onrender.com/docs](https://book-tracker-api-0ejh.onrender.com/docs). The docs are customised to the project with example values.

## API Routes
* `POST /auth/register`: Create a new user account with a username and password.
* `POST /auth/login`: Login with your username and password to receive a JWT access token.
* `GET /users/me`: Retrieve the details of the currently authenticated user.
* `GET /users/me/stats`: Retrieve statistics about the user's reading progress.
* `GET /books/`: Retrieve a list of all books added by the current user.
* `GET /books/{book_id}`: Retrieve the details of a specific book by its ID.
* `POST /books/create`: Add a new book to your tracking with its Title, Author, and Total Pages.
* `PUT /books/update/{book_id}`: Update the number of pages read for a specific book.
* `DELETE /books/delete/{book_id}`: Remove a book from your tracking list by its ID.

![ss](/assets/ss.png)

## Setup and Installation

```bash
git clone https://github.com/MrKillerShaunBa/Book-Tracker-API
cd Book-Tracker-API
python -m venv api_venv
api_venv\Scripts\activate # For Windows
source api_venv/bin/activate # For Linux 
pip install -r requirements.txt
uvicorn app.main:app --reload
```
You can use the API at `http://127.0.0.1:8000` and the docs at `http://127.0.0.1:8000/docs`

## Tech Stack

* **Backend**: Python 3, FastAPI
* **Database**: SQLite, SQLAlchemy and Pydantic
* **Server**: Uvicorn
* **Authentication**: JWT
* **Hosting**: Render





