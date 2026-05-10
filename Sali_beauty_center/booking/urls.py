from django.urls import path
from .views import home, ServiceListView, service_detail, about

app_name = 'booking'

urlpatterns = [
    path('', home, name='home'),
    path('services/', ServiceListView.as_view(), name='services'),
    path('services/<int:service_id>/', service_detail, name='service_detail'),
    path('about/', about, name='about'),
]