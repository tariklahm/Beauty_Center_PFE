from django.urls import path
from .views import employee_detail, user_login

app_name = 'users'

urlpatterns = [
    path('employee/<int:employee_id>/<int:service_id>/', employee_detail, name='employee_detail'),
    path('login/', user_login, name = 'login'),
]