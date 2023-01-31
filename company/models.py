from django.db import models

# Create your models here.
class Post(models.Model):
  # field_name = models.fieldType()
  title = models.CharField(max_length=80)
  description = models.TextField(max_length=160)
  body = models.TextField()
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

class ProductDeme(models.Model):
  name = models.CharField(max_length=100)
  detail = models.TextField(null=True, blank=True)
  price = models.FloatField(default=1)
  instock = models.BooleanField(default=True)

  def __str__(self):
    return self.name
# 1. models
# makemigrations -- update database
# migrate -- submit table

# Set title name

# 2. admin
# register: display to admin page

# 3. Views