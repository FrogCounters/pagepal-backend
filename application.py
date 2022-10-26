import uuid
from models import *
from helpers import *
from firestore import *
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# uvicorn application:app --reload
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
        # print(doc, doc.to_dict())
        books_list.append(doc.id)
    return {"books": books_list}


@app.get("/book/{title}")
async def get_book_document(title):
    doc = get_book(title)
    return {title: doc}


@app.post("/book")
async def create_book_document(book: Book):
    insert_book(book.title, book.url, book.text, book.emotions, book.hate_speech, book.author, book.main_img)
    return JSONResponse(content={"success": "true"}, status_code=200)


@app.post("/analyse")
async def analyse_user_book(user: UserText):
    emotions_list = []
    for sentence in user.text.split("."):
        emotions_list.append(analyse_text(sentence))
    return {"emotions": emotions_list}


@app.get("/user_book/{book_id}")
async def get_user_book_document(book_id):
    doc = get_user_book(book_id)
    return {book_id: doc}


@app.post("/user_book")
async def create_user_book_document(book: UserUrlBook):
    book_id = str(uuid.uuid4().hex)[:16]
    insert_user_book(book.title, book.text, book.emotions, book.hate_speech, book_id)
    return JSONResponse(content={"url": book_id}, status_code=200)
