# Book Tracker API

This is FastAPI based Book Tracker which allows you to save the progress (number of pages read) of the books you are reading. It helps to keep a track of the books you have finished, currently reading and not started. My motivation to build this was that I have a large library of books at home and have a hard time remembering where I left a particular book when I didnt use a bookmark. I plan to add a front-end to this in the future.

## Hosted API Docs

You can see the hosted Swagger docs [here]().

## API Routes
* `POST /auth/register`: Register a new user
* `POST /auth/login`: Obtain a JWT access token
* `GET /users/me`: Fetch username and userID of the current user
* `GET /users/me/stats`: Get the book reading statistics of the current user
* `GET /books/`: View all the books and their details register by the current user
* `GET /books/{book_id}`: View the details of a single book using their unique assigned book_id
* `POST /books/create`: Add the details of a new book to your account
* `PUT /books/{book_id}`: Log number of pages read of that book
* `DELETE /books/{book_id}`: Delete the record of a particular book
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
