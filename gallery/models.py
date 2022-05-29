from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =60)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()    

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(name=value)
    


class Category (models.Model):
    name = models.CharField(max_length =60)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()   

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(name=value)
     

class Image(models.Model):
    photo = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =60)
    description = models.CharField(max_length =300)
    location = models.ForeignKey(Location , on_delete=models.CASCADE, default ='location')
    category = models.ForeignKey(Category, on_delete=models.CASCADE , default ='')
   
    def __str__(self):
        return self.name

    class Meta:
        ordering =['name']

    def save_image(self):
        self.save()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(photo =value)

    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__name__icontains=search_term) 
        return images

    @classmethod 
    def filter_by_location(cls, location):
        image_location =Image.objects.filter(location_name=location).all()       
        return image_location
