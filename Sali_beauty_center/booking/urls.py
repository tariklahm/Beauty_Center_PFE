from django.urls import path
from .views import home, services, about

app_name = 'booking'

urlpatterns = [
    path('', home, name='home'),
    path('services/', services, name='services'),
    path('about/', about, name='about'),
]