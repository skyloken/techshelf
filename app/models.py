from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Author(models.Model):
    """Book Author"""
    name = models.CharField('著者名', max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Book Tag"""
    name = models.CharField('タグ名', max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Book"""
    isbn = models.CharField('ISBN', max_length=13)
    title = models.CharField('書籍名', max_length=200)
    subtitle = models.CharField('サブタイトル', max_length=200, blank=True, null=True)
    authors = models.ManyToManyField(Author, verbose_name='著者')
    tags = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)
    published_date = models.DateField('発刊日')
    description = models.TextField('説明')
    image_link = models.URLField('画像URL')
    info_link = models.URLField('書籍情報URL')

    def __str__(self):
        return self.title


class Review(models.Model):
    """Review for the Book"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews',
                             verbose_name='レビューユーザ')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='対象の本')
    score = models.IntegerField('スコア', validators=[MinValueValidator(1), MaxValueValidator(5)])
    title = models.CharField('タイトル', max_length=200)
    reason = models.TextField('読んだ理由')
    body = models.TextField('レビュー')
    likes = models.ManyToManyField(get_user_model(), related_name='likes', verbose_name='いいねしたユーザ', blank=True)
    reviewed_at = models.DateTimeField('レビュー日時', auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment on the Review"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='コメントユーザ')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, verbose_name='対象のレビュー')
    body = models.TextField('コメント')
    commented_at = models.DateTimeField('コメント日時')

    def __str__(self):
        return self.body


class Mark(models.Model):
    """Mark for the Book"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='マークユーザ')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='対象の本')
    comment = models.TextField('コメント', blank=True, null=True)
    marked_at = models.DateTimeField('マーク日時')

    def __str__(self):
        return self.comment
