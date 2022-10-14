from models import *
from firestore import *
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# uvicorn main:app --reload
# https://fastapi.tiangolo.com/tutorial/path-params/
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/books")
async def get_books_document():
    docs = get_all_books()
    books_list = []
    for doc in docs:
        print(doc, doc.to_dict())
        books_list.append(doc.id)
    return {"books": books_list}


@app.get("/book/{title}")
async def get_book_document(title):
    doc = get_book(title)
    return {title: doc}


@app.post("/book")
async def create_book_document(book: Book):
    # print(book.text)
    insert_book(book.title, book.url, book.text, book.emotions, book.author, book.main_img)
    return JSONResponse(content={"success": "true"}, status_code=200)
