from django.shortcuts import render
from users.models import Employee
from .models import Service

def home(request):
    employees = Employee.objects.all()

    context = {
        'employees': employees
    }

    return render(request, 'home.html', context)

# retreive available services
def services(request):
    services = Service.objects.all()

    context = {
        'services': services
    }

    return render(request, 'booking/services.html', context)

def about(request):
    return render(request, 'about.html')