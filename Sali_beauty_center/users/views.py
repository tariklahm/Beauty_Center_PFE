from django.shortcuts import render, get_object_or_404
from .models import Employee
from booking.models import Service
from django.http import HttpResponse
from . forms import LoginForm

def employee_detail(request, employee_id, service_id):
    employee = get_object_or_404(Employee, id=employee_id)
    service = get_object_or_404(Service, id=service_id)
    category = service.category

    return render(request, "users/employee_detail.html", {
        "employee": employee,
        "service": service,
        "category": category,
    })

def user_login(request):
    form = LoginForm()
    
    return render(request, 'users/auth/login.html', {'form': form})
