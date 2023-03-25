from django.urls import path, include
from . import views
urlpatterns = [
    path('books/', views.get_all_books, name = 'books')
]
