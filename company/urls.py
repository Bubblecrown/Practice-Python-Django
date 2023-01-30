from django.urls import path
from .views import Homepage, About

urlpatterns = [
    # path('URL name', function name)
    path('', Homepage),
    path('about', About)
]