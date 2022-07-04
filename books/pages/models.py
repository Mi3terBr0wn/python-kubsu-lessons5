from django.db import models

# Create your models here.

class Genre(models.Model):

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    name = models.CharField(max_length=30, verbose_name='Жанр', unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    name = models.CharField(max_length=40, verbose_name='Автор')

    def __str__(self):
        return self.name

class Book(models.Model):

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    book_name = models.TextField(verbose_name='Название')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, verbose_name='Жанр')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, verbose_name='Автор')