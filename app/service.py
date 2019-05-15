import requests
from dateutil.parser import parse

from .models import *

url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'


def get_book_info(book):
    # Google Books API から本情報を取得
    req_url = url + book.isbn
    response = requests.get(req_url)
    data = response.json()['items'][0]['volumeInfo']

    # 本情報を登録
    book.title = data['title']
    if 'subtitle' in data:
        book.subtitle = data['subtitle']
    book.description = data['description']
    book.image_link = data['imageLinks']['thumbnail']
    book.info_link = data['infoLink']
    book.published_date = parse(data['publishedDate']).date()
    book.save()

    # 著者検索・登録
    book_authors = data['authors']
    for book_author in book_authors:
        author, created = Author.objects.get_or_create(name=book_author)
        book.authors.add(author)

    return book
