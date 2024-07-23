from django.db import models

# Create your models here.

class New_post(models.Model):
    tag = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='db image')
    date = models.DateField()
    author = models.CharField(max_length=100)
    link = models.CharField(max_length=300)

