from django.db import models
import datetime as dt

# Create your models here.
class Images(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.ImageField(upload_to = 'images/')
    description = models.TextField()
    posted = models.DateTimeField(auto_now_add = True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering =['title']

    def save_pixxies(self):
        self.save()

    @classmethod
    def get_pixxies(cls):
        images = cls.objects.all()

        return images

    @classmethod
    def search_by_category(cls,search_term):
        details = cls.objects.filter(category__icontains=search_term)
        return details


class Category(models.Model):
    categ = models.CharField(max_length=50)

class Location(models.Model):   
    locate = models.CharField(max_length=50)


