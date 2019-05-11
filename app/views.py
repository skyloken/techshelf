from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Book, Review
from .forms import CustomUserCreationForm, AddBookForm
from .service import get_book_info


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'app/signup.html'


def index(request):
    review_list = Review.objects.order_by('-reviewed_at')
    context = {'reviews_page': 'active', 'review_list': review_list}
    return render(request, 'app/index.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {'reviews_page': 'active', 'review': review}
    return render(request, 'app/review_detail.html', context)


def books(request):
    if request.method == "POST":
        add_book_form = AddBookForm(request.POST)
        if add_book_form.is_valid():
            # 新規本追加処理
            book = get_book_info(add_book_form.save(commit=False))
            return redirect('book_detail', book_id=book.id)
    else:
        add_book_form = AddBookForm()
        book_list = Book.objects.order_by('title')
        context = {'books_page': 'active', 'book_list': book_list, 'add_book_form': add_book_form}
        return render(request, 'app/books.html', context)


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'books_page': 'active', 'book': book}
    return render(request, 'app/book_detail.html', context)
