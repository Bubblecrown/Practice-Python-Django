from django.urls import path
from .views import *

urlpatterns = [
    # path('URL name', function name)
    path('', Homepage),
    path('contact', Contact),
    path('product', Product),
    path('blog/<int:id>', post_detail),
    path('search', Search),
    path('addBook', AddBook),
    path('bookList', BookList)
]