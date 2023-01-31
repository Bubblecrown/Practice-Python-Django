from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, ProductDeme

def Homepage(request):
  # variable = Table.objects.method()
  all_posts = Post.objects.all()

  # Data that send to html must be in dictionary
  # {'key' : value}
  return render(request, 'company/Home.html', {'all_posts':all_posts})
  

def About(request):
  data = ProductDeme.objects.all()
  context = {'data': data}
  return render(request, 'company/about.html', context)



def Product(request):
  data = ProductDeme.objects.all()
  context = {'data': data}
  return render(request, 'company/product.html', context)