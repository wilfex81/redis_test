from django.shortcuts import render
from django.conf import settings

#cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from .models import MyLibrary

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
def get_all_books(request):
    books = MyLibrary.objects.all()
    # context = {
    #     books : "books"
    # }
    return render(request, 'lib.html', { 'books' : books})
