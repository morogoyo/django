from django.db import models

# Create your models here
class Article(models.Model):
    headline= models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    content = models.TextField()