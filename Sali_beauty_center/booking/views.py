from django.shortcuts import render, get_object_or_404
from users.models import Employee
from .models import Service
from django.views.generic import ListView

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
    template_name = 'booking/services.html'
# Service detail
def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    employees = Employee.objects.filter(services=service)

    context = {
        'service': service,
        'employees': employees
    }
    return render(request, 'booking/service_detail.html', context)

# The about page view
def about(request):
    return render(request, 'about.html')