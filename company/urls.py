from django.urls import path
from .views import Homepage, About, Product, post_detail

urlpatterns = [
    # path('URL name', function name)
    path('', Homepage),
    path('about', About),
    path('product', Product),
    path('blog/<int:id>', post_detail)
]