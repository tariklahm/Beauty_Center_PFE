from django.db import models
from django.contrib.auth.models import User


# create a profile model
class Profile(models.Model):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('employee', 'Employee'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default= 'client')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
# create Employees model

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    services = models.ManyToManyField('booking.Service')
     
    availability = models.CharField(max_length=255)

    image = models.ImageField(upload_to='employees/', blank=True, null=True)

    bio = models.TextField()
    experience_years = models.PositiveIntegerField()
    diplomas = models.TextField()

    def __str__(self):
        return self.user.username
    

