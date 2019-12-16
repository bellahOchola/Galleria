from django.test import TestCase
]from .models import Images, Category, Location

# Create your tests here.
class ImagesTestClass(TestCase):

    def setUp(self):
        self.image = Images(title = 'Gasier', description = 'music is my thing', category = 'Music', location = 'Kisumu')

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Images))

    def test_save_images(self):
        self.image.save_pixxies()
        images = Images.objects.all()
        self.asserTrue(len(images)>0)

    def test_delete_images(self):
        self.image.delete_pixxies()
        images = Images.objects.all()
        self.asserTrue(len(images) == 0)