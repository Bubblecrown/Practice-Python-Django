from django.urls import path
from .views import Homepage, About, Product

urlpatterns = [
    # path('URL name', function name)
    path('', Homepage),
    path('about', About),
    path('product', Product)
]