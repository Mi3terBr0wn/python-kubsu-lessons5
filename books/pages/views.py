from django.shortcuts import render, redirect, HttpResponse
from .models import Author, Book, Genre
from .forms import AddAuthor, AddBook, AddGenre

# Create your views here.


def index(request):
    ctx = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
        'genres': Genre.objects.all()
    }
    return render(request, 'pages/index.html', ctx)


def book(request, id):
    book = Book.objects.get(pk=id)
    if request.POST:
        form = AddBook(request.POST)
        if form.is_valid():
            book.genre = form.cleaned_data['genre']
            book.author = form.cleaned_data['author']
            book.book_name = form.cleaned_data['book_name']
            book.save(update_fields=['genre', 'author', 'book_name'])
        else:
            return HttpResponse('Форма введена с ошибкой')
    form = AddBook()
    ctx = {
        'book': book,
        'form': form
    }
    return render(request, 'pages/book.html', ctx)


def genre(request, id):
    genre = Genre.objects.get(pk=id)
    if request.POST:
        form = AddGenre(request.POST)
        if form.is_valid():
            genre.name = form.cleaned_data['name']
            genre.save(update_fields=['name'])
        else:
            return HttpResponse('Форма введена с ошибкой')
    form = AddGenre()
    ctx = {
        'genre': genre,
        'form': form
    }
    return render(request, 'pages/genre.html', ctx)

def author(request, id):
    author = Author.objects.get(pk=id)
    if request.POST:
        form = AddAuthor(request.POST)
        if form.is_valid():
            author.name = form.cleaned_data['name']
            author.save(update_fields=['name'])
        else:
            return HttpResponse('Форма введена с ошибкой')
    form = AddAuthor()
    ctx = {
        'author': author,
        'form': form
    }
    return render(request, 'pages/author.html', ctx)


def add_genre(request):
    if request.POST:
        form = AddGenre(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('Форма введена с ошибкой')
    else:
        form = AddGenre()
    ctx = {
        'form': form
    }
    return render(request, 'pages/add_genre.html', ctx)


def add_author(request):
    if request.POST:
        form = AddAuthor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('Форма введена с ошибкой')
    else:
        form = AddAuthor()
    ctx = {
        'form': form
    }
    return render(request, 'pages/add_author.html', ctx)


def add_book(request):
    if request.POST:
        form = AddBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('Форма введена с ошибкой')
    else:
        form = AddBook()
    ctx = {
        'form': form
    }
    return render(request, 'pages/add_book.html', ctx)