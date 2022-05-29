from django.test import TestCase
from .models import Image, Location, Category
# Create your tests here.


class LocationTestClass(TestCase):


    def setUp(self):
        self.location = Location( name = 'South Africa' )
        self.location.save_location()


    def tearDown(self):
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_method(self):
        self.location.save_location()
        locations= Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_update_methode(self):
        self.location.save_location()
        new_location='Peru'
        self.location.update_location(self.location.id, new_location)
        update = Location.objects.get(name='Peru')
        self.assertEquals(update.name, 'Peru')

    def test_delete_method(self):
        self.location.save_location()
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

class CategoryTestClass(TestCase):

    def setUp(self):
        self.category = Category(name = 'Travel' )
        self.category.save_category()

    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    def test_save_method(self):
        self.category.save_category()
        categories= Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_update_methode(self):
        self.category.save_category()
        new_category='Family'
        self.category.update_category(self.category.id, new_category)
        update = Category.objects.get(name='Family')
        self.assertEquals(update.name, 'Family')

    def test_delete_method(self):
        self.category.save_category()
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)
    

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.image = Image( name = 'South Africa', description = 'This was during the World tour of Ed Sheeran',location=self.location, category =self.category)

        self.category = Category(name='Family')
        self.category.save_category()

        self.location = Location(name='Peru')
        self.location.save_location()
 

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    # def save_image(self):
    #     self.save()

    
    # def test_save_method(self):
    #     self.image.save_image()
    #     images =Image.objects.all()
    #     self.assertTrue(len(images)>0)

    # def test_update_methode(self):
    #     self.photo.save_image()
    #     self.photo.update_image(self.photo.id,'images/photo.jpg')
    #     new_photo = Image.objects.filter(photo='images/photo.jpg')
    #     self.assertTrue(len(new_photo)>0)

    # def test_delete_method(self):
    #     self.image.delete_image()
    #     images =Image.objects.all()
    #     self.assertTrue(len(images) == 0)

    # def test_get_image_by_id(self):
    #     self.image.save_image()
    #     image_found = self.image.get_image_by_id(self.image.id)
    #     self.assertTrue(len(image_found)>0)

    # def test_search_image_by_category(self):
    #     self.image.save_image()
    #     searched_photo = self.image.filter_by_category('Family')
    #     self.assertTrue(len(searched_photo)>0)

    # def test_filter_by_location(self):
    #     self.adventure.save_image()
    #     filtered_photo = self.adventure.filter_by_location(location='Peru')
    #     self.assertTrue(len(filtered_photo)>0)
