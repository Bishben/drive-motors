from django.db import models

# Create your models here.

car_makes = (("Toyota","Toyota"),("Nissan","Nissan"),("Mitsubishi","Mitsubishi"),("Lexus","Lexus"),("Hyundai","Hyundai"),("Renault","Renault"),("BMW","BMW"))
car_conditions = (("New","New"),("Old","Old"))
featured_options = (("Yes","Yes"),("No","No"))
color_options = (("White","White"),("Black","Black"),("Gray","Gray"),("Silver","Silver"),("Red","Red"),("Blue","Blue"),("Brown","Brown"),("Green","Green"),("Beige","Beige"),("Orange","Orange"),("Gold","Gold"),("Yellow","Yellow"),("Purple","Purple"))

class car(models.Model):
    name = models.CharField(max_length=100,unique=True)
    image_one = models.ImageField(upload_to = 'static/images')
    image_two = models.ImageField(upload_to = 'static/images')
    image_three = models.ImageField(upload_to = 'static/images', blank = True)
    image_four = models.ImageField(upload_to = 'static/images', blank = True)
    make = models.CharField(max_length=100, choices = car_makes)
    model = models.CharField(max_length = 100)
    condition = models.CharField(max_length=100, choices = car_conditions)
    price = models.IntegerField()
    kilometers = models.IntegerField()
    color = models.CharField(max_length=50, choices = color_options)
    featured = models.CharField(max_length=10, choices = featured_options, default = "No")

    def __str__(self):
        return self.name
