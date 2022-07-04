from django.urls import path
from . import views


appname = 'pages'
urlpatterns = [
    path('', views.index, name='home'),
    path('book/<int:id>', views.book, name='book'),
    path('add_book', views.add_book, name='add_book'),
    path('genre/<int:id>', views.genre, name='genre'),
    path('add_genre', views.add_genre, name='add_genre'),
    path('author/<int:id>', views.author, name='author'),
    path('add_author', views.add_author, name='add_author'),
]