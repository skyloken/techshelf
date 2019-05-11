from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Book


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

    fields = UserCreationForm.Meta.fields + ('icon', 'bio')


class AddBookForm(forms.ModelForm):
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
