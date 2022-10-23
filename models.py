from pydantic import BaseModel


class Book(BaseModel):
    title: str
    url: str
    text: list
    emotions: list
    author: str
    main_img: str


class UserText(BaseModel):
    text: str