from django.contrib import admin
from .models import Service, AppointmentService, Payment, Appointment

# for more organisation of admin panel
# admin.site.register(Service)
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'duration')
    list_filter = ('category',)
    search_fields = ('name',)

admin.site.register(Appointment)
admin.site.register(AppointmentService)
admin.site.register(Payment)