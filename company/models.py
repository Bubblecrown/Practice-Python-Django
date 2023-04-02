from django.db import models

# Create the table

class Post(models.Model):
  # field_name = models.fieldType()
  title = models.CharField(max_length=80)
  description = models.TextField(max_length=160)
  body = models.TextField()
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)
  cover_image = models.ImageField(upload_to="cover/", null=True, blank=True)

  def __str__(self):
    return self.title

class ProductDeme(models.Model):
  name = models.CharField(max_length=100)
  detail = models.TextField(null=True, blank=True)
  price = models.FloatField(default=1)
  instock = models.BooleanField(default=True)

  def __str__(self):
    return self.name
  
class Contact(models.Model):
  subject = models.CharField(max_length=150)
  email = models.EmailField(null=True)
  sender = models.CharField(max_length=80)
  detail = models.TextField()
  date_sent = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.subject

# 1. models
# python manage.py makemigrations -- update database
# python manage.py migrate -- submit table
# ***** update set null *****

# Set title name

# 2. admin
# register: display to admin page

# 3. Views

