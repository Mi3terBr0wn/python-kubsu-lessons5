from django.forms import models

from .models import Genre, Author, Book


class AddGenre(models.ModelForm):

    class Meta:
        model = Genre
        fields = ('name',)


class AddAuthor(models.ModelForm):

    class Meta:
        model = Author
        fields = ('name',)


class AddBook(models.ModelForm):

    class Meta:
        model = Book
        fields = ('book_name', 'genre', 'author')
