from django.contrib import admin
from .models import Book, Contact, Post, ProductDeme
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
  # replace body field
  summernote_fields = ('body')
  list_display = ['title', 'date_created', 'date_updated']

# class : admin.site.register(Model, ModelAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(ProductDeme)
admin.site.register(Contact)
admin.site.register(Book)