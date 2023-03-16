from fastapi import FastAPI
from . import schemas
from . import database

app = FastAPI()

@app.get("/")
def get_root():
	return "Welcome to the books api"

@app.post("/book/")
def create_book(request: schemas.BookAuthorPayload):
	database.add_book(convert_into_book_db_model(request.book), convert_into_author_db_model(request.author))
	return "New book added " + request.book.title + " " + str(request.book.number_of_pages) \
	+ " New author added " + request.author.first_name + " " + request.author.last_name

def convert_into_book_db_model(book: schemas.Book):
	return database.Book(title=book.title, number_of_pages=book.number_of_pages)

def convert_into_author_db_model(author: schemas.Author):
	return database.Author(first_name=author.first_name, last_name=author.last_name)