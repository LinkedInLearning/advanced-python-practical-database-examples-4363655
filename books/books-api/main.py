from fastapi import FastAPI
from . import schemas

app = FastAPI()

@app.get("/")
def get_root():
	return "Welcome to the books api"

@app.post("/book/")
def create_book(request: schemas.BookAuthorPayload):
	return "New book added " + request.book.title + " " + str(request.book.number_of_pages) \
	+ " New author added " + request.author.first_name + " " + request.author.last_name

