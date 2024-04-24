from django.db import models

# Create your models here.
from django.core.validators import RegexValidator

class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be exactly 10 digits.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10)
    email = models.EmailField(unique=True)  # Required and unique email field
    assigned_helper = models.OneToOneField('Helper', on_delete=models.SET_NULL, null=True, blank=True, related_name='customer')

    def __str__(self):
        return self.name
    
class Helper(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    name = models.CharField(max_length=100,unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    skill = models.CharField(max_length=100)
    age = models.IntegerField()
    # Add more fields as needed

    def __str__(self):
        return self.name