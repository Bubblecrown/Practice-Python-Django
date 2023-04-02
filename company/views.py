from django.shortcuts import redirect, render
from django.http import HttpResponse

from .form import ContactForm
from django.db.models import Q
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

def Contact(request):
  view = 'company/contact.html'
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid:
      # save to DB
      form.save()
      return redirect("/")
  else:
    form = ContactForm()
  context = {'form' : form}
  return render(request, view, context)

def Product(request):
  view = 'company/product.html'
  data = ProductDeme.objects.all()
  context = {'data': data}
  return render(request, view, context)

def Search(request):
  view = 'company/search.html'
  search_post = request.GET.get('q')
  if search_post:
    post = Post.objects.filter(Q(title__icontains = search_post))
  else:
    pass
  context = {'post' : post}

  return render(request, view, context)

# .\venv\Scripts\activate
# cd firstweb
# python manage.py runserver