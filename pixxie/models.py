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

    def delete_pixxies(self):
        self.delete()

    @classmethod
    def get_pixxies(cls):
        images = cls.objects.all()

        return images

    # @classmethod
    # def get_pixxies_cat(cls,categ):
    #     categ_pixxies = cls.objects.filter(category = categ)
    #     print (categ_pixxies)

    #     return categ_pixxies

    @classmethod
    def search_category(cls,search_term):
        category = cls.objects.filter(category__categ__icontains=search_term)

        return category

    
    @classmethod
    def pixxies_by_loct(cls, location):
        loct_pixxies = Images.objects.filter(location__locate=location).all()

        return loct_pixxies


class Category(models.Model):
    categ = models.CharField(max_length=50)

    def __str__(self):
        return self.categ

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    
        

class Location(models.Model):   
    locate = models.CharField(max_length=50)
    
    @classmethod
    def get_location(cls):
        location = cls.objects.all()

        return location
