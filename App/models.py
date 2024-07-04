from django.db import models

# Create your models here.
# class user_data(models.Model):
#   name = models.CharField(max_length=255)
#   email = models.CharField(max_length=255,)
#   password = models.CharField(max_length=255)

class Form_data(models.Model):
    f_name = models.CharField(max_length=20, blank=True, null=True)
    l_name = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=144, blank=True, null=True)
    phone_number = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)

class profileImages(models.Model):
    image = models.ImageField(upload_to='images/')