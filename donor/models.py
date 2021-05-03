from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Donor(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    phone = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    dod = models.DateField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    is_authenticated = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return "%s" %self.username

class DonationHistory(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    dod = models.DateField()
    units = models.IntegerField()
    purpose = models.TextField()