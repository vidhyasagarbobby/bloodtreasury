from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    phone = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    website = models.URLField(max_length=200)
    address = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    is_authenticated = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.id
    
    # def get_absolute_url(self):
    #     return "%i" %self.id