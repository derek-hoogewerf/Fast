# main.py
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from pydantic.types import UrlStr

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


@app.put("/items/{item_id}")
async def create_multiple_images(images: list[Image]):
    results = {"item_id": item_id, "item": item}
    return results
