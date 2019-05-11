import requests
from .models import *
from django.http import Http404
from dateutil.parser import parse

url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'


def get_book_info(book):
    # Google Books API から本情報を取得
    req_url = url + book.isbn
    response = requests.get(req_url)

    # 本が存在するかチェック
    data = response.json()
    if data['totalItems'] == 0:
        raise Http404
    book_data = data['items'][0]['volumeInfo']

    # 同じ本がすでに存在する場合かチェック
    if Book.objects.filter(isbn=book.isbn).exists():
        raise Http404

    # 本情報を登録
    book.title = book_data['title']
    book.description = book_data['description']
    book.image_link = book_data['imageLinks']['thumbnail']
    book.info_link = book_data['infoLink']
    book.published_date = parse(book_data['publishedDate']).date()
    book.save()

    # 著者検索・登録
    book_authors = book_data['authors']
    for book_author in book_authors:
        author, created = Author.objects.get_or_create(name=book_author)
        book.authors.add(author)

    return book
