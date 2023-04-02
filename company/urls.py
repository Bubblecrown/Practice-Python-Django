from django.urls import path
from .views import (Homepage, Contact, Product, post_detail, Search)

urlpatterns = [
    # path('URL name', function name)
    path('', Homepage),
    path('contact', Contact),
    path('product', Product),
    path('blog/<int:id>', post_detail),
    path('search', Search)
]