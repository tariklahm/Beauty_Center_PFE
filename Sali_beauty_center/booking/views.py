from django.shortcuts import render, get_object_or_404, redirect
from users.models import Employee
from .models import Service
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
def home(request):
    employees = Employee.objects.all()

    context = {
        'employees': employees
    }

    return render(request, 'home.html', context)

# retreive available services
# def services(request):
#     services = Service.objects.all()

#     context = {
#         'services': services
#     }

#     return render(request, 'booking/services.html', context)

# services class view and Pagination 
class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'
    paginate_by = 6
    template_name = 'booking/services/services.html'

# Service detail
def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    employees = Employee.objects.filter(services=service)

    context = {
        'service': service,
        'employees': employees
    }
    return render(request, 'booking/services/service_detail.html', context)
#services_categorie page
def services_categories(request):
    return render(request, 'booking/services/services_categories.html')

# Category_detail
def category_detail(request, category):
    
    services = Service.objects.filter(category=category)

    context = {
        'services': services,
        'category': category,
    }
    return render(request, 'booking/services/category_detail.html', context)
# The about page view
def about(request):
    return render(request, 'about.html')

# making appointement view
@login_required
def create_appointment(request, employee_id):

    employee = get_object_or_404(
        Employee,
        id=employee_id
    )

    form = AppointmentForm()
    # show only services this employee can do
    form.fields['services'].queryset = employee.services.all()
    
    context = {
        'form': form,
        'employee': employee
    }

    return render(
        request,
        'booking/appointments/create_appointment.html',
        context
    )