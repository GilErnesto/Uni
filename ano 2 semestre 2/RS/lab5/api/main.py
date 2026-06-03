from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Books API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_TOKEN = "secret-token"


class Book(BaseModel):
    title: str
    author: str
    year: int
    genre: str


class BookOut(Book):
    id: int


books: list[BookOut] = [
    BookOut(id=1, title="Ensaio sobre a Cegueira", author="José Saramago", year=1995, genre="Literary Fiction"),
    BookOut(id=2, title="Mensagem", author="Fernando Pessoa", year=1934, genre="Poetry"),
    BookOut(id=3, title="Os Lusíadas", author="Luís de Camões", year=1572, genre="Epic Poetry"),
    BookOut(id=4, title="Amor de Perdição", author="Camilo Castelo Branco", year=1862, genre="Romanticism"),
    BookOut(id=5, title="O Filho de Mil Homens", author="Valter Hugo Mãe", year=2011, genre="Literary Fiction"),
]

next_id = 6


def find_book(book_id: int) -> BookOut:
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books", response_model=list[BookOut])
def list_books(author: Optional[str] = None):
    if author:
        return [b for b in books if author.lower() in b.author.lower()]
    return books


@app.get("/books/{book_id}", response_model=BookOut)
def get_book(book_id: int):
    return find_book(book_id)


@app.post("/books", response_model=BookOut, status_code=201)
def create_book(book: Book):
    global next_id
    new_book = BookOut(id=next_id, **book.model_dump())
    books.append(new_book)
    next_id += 1
    return new_book


@app.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, book: Book):
    existing = find_book(book_id)
    updated = BookOut(id=book_id, **book.model_dump())
    books[books.index(existing)] = updated
    return updated


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    existing = find_book(book_id)
    books.remove(existing)


@app.get("/books/{book_id}/read")
def read_book(book_id: int, authorization: Optional[str] = Header(default=None)):
    if authorization != f"Bearer {SECRET_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    book = find_book(book_id)
    return {"message": f"Now reading: {book.title} by {book.author}"}
