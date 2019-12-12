from django.db import models

# Create your models here.
class Images(models.Model):
    image_url = models.ImageField()
    description = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)