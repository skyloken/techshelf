import requests
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import MinLengthValidator
from django_starfield import Stars

from .models import Book, Review

url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

    fields = UserCreationForm.Meta.fields + ('icon', 'bio')


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'uk-input uk-form-large'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['class'] = 'uk-input uk-form-large'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class AddBookForm(forms.ModelForm):
    """本追加フォーム"""

    class Meta:
        model = Book
        fields = ('isbn',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['isbn'].widget.attrs['class'] = 'uk-input'
        self.fields['isbn'].widget.attrs['placeholder'] = 'ISBN'

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']

        # Googleブックスに存在するかをチェック
        req_url = url + isbn
        response = requests.get(req_url)
        data = response.json()
        if data['totalItems'] == 0:
            raise forms.ValidationError('この本はGoogleブックスに存在しません')

        # ISBN-10の場合，ISBN-13に変換して重複チェック
        if len(isbn) == 10:
            identifiers = data['items'][0]['volumeInfo']['industryIdentifiers']
            for identifier in identifiers:
                if identifier['type'] == 'ISBN_13':
                    isbn_13 = identifier['identifier']
                    if Book.objects.filter(isbn=isbn_13).exists():
                        raise forms.ValidationError('この本は既に登録済みです')
                    else:
                        isbn = isbn_13

        return isbn


class PostReviewForm(forms.ModelForm):
    """レビュー投稿フォーム"""

    score = forms.IntegerField(
        label='',
        max_value=5.0,
        min_value=1.0,
        required=True,
        initial=1,
        widget=Stars,
    )

    class Meta:
        model = Review
        fields = ('score', 'title', 'reason', 'body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'uk-input'})
        self.fields['reason'].widget.attrs.update({'class': 'uk-textarea', 'rows': 3})
        self.fields['body'].widget.attrs.update({'class': 'uk-textarea', 'rows': 8})
