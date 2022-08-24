from django.db import models


class Smart_phone(models.Model):
    brand = models.CharField( max_length=30, null=False)
    phone_name = models.CharField( max_length=50, null=False)
    phone_colour = models.CharField( max_length=10, null= True)
    phone_images = models.ImageField( upload_to="phone_image",blank=True)
    storage = models.IntegerField()
    avalablity = models.BooleanField(default=True)

class Smart_watch(models.Model):
    brand = models.CharField( max_length=20, null=False)
    name = models.CharField(max_length=30,null= False)
    watch_colour = models.CharField( max_length=10, null= True)
    watch_images = models.ImageField( upload_to="watch_image",blank=True)
    size = models.IntegerField()
    avalablity = models.BooleanField(default=True)
