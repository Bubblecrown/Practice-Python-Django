from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, ProductDeme

def Homepage(request):
  view = 'company/Home.html'
  # variable = Table.objects.method()
  all_posts = Post.objects.all()
  context = {'all_posts':all_posts}
  # Data that send to html must be in dictionary
  # {'key' : value}
  return render(request, view, context)
  
def post_detail(request, id):
  view = 'company/post-detail.html'

  # single post
  data = Post.objects.get(id=id)
  context = {'data': data}
  return render(request, view, context)

def About(request):
  view = 'company/about.html'
  data = ProductDeme.objects.all()
  context = {'data': data}
  return render(request, view, context)

def Product(request):
  view = 'company/product.html'
  data = ProductDeme.objects.all()
  context = {'data': data}
  return render(request, view, context)