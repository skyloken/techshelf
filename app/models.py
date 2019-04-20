from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Author(models.Model):
    """Book Author"""
    name = models.CharField(max_length=200)


class Tag(models.Model):
    """Book Tag"""
    name = models.CharField(max_length=200)


class Book(models.Model):
    """Book"""
    isbn = models.IntegerField(max_length=13)
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    tags = models.ManyToManyField(Tag)
    published_date = models.DateField()
    description = models.TextField()
    image_link = models.URLField()
    info_link = models.URLField()


class Review(models.Model):
    """Review for the Book"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    score = models.IntegerField()
    title = models.CharField(max_length=200)
    reason = models.TextField()
    body = models.TextField()
    likes = models.ManyToManyField(get_user_model())
    reviewed_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    """Comment on the Review"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    body = models.TextField()
    commented_at = models.DateTimeField()


class Mark(models.Model):
    """Mark for the Book"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    marked_at = models.DateTimeField()
