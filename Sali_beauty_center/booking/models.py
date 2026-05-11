from django.db import models
from django.contrib.auth.models import User


# creat service Model
class Service(models.Model):

    CATEGORY_CHOICES = [
        ('hair', 'Hair'),
        ('nails', 'Nails'),
        ('facial', 'Face'),
        ('body', 'Body'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.IntegerField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='hair')

    def __str__(self):
        return self.name

# creat Appointement Model
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    employee = models.ForeignKey('users.Employee', on_delete=models.CASCADE, related_name='appointments')
    
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    
    
    def __str__(self):
        return f"{self.client.username} - {self.date}"
    
# creat AppointmentService model

class AppointmentService(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='services')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointment_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)  # snapshot price

    def __str__(self):
        return f"{self.appointment} - {self.service.name}"

    class Meta:
        unique_together = ('appointment', 'service')

# Creat Payment model

class Payment(models.Model):
    STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('paid', 'Paid'),
    ('failed', 'Failed'),
]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id}"
    
