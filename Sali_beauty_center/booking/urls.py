from django.urls import path
from .views import home, ServiceListView, service_detail,services_categories, category_detail,about, create_appointment

app_name = 'booking'

urlpatterns = [
    path('', home, name='home'),
    path('services/', ServiceListView.as_view(), name='services'),
    path('services/<int:service_id>/', service_detail, name='service_detail'),
    path('services_categories/', services_categories, name='services_categories'), #
    path('services/<str:category>/', category_detail, name='category_detail'),
    path('appointment/<int:employee_id>/', create_appointment, name='create_appointment'),


    path('about/', about, name='about'),
]