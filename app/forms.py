from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django_starfield import Stars

from .models import Book, Review


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

    fields = UserCreationForm.Meta.fields + ('icon', 'bio')


class AddBookForm(forms.ModelForm):
    """本追加フォーム"""
    isbn = forms.CharField(
        max_length=13,
        min_length=13,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'uk-input',
                'placeholder': 'ISBN'
            }
        )
    )

    class Meta:
        model = Book
        fields = ('isbn',)


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
