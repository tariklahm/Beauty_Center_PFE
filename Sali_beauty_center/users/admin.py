from django.contrib import admin
from .models import Profile, Employee

admin.site.register(Profile)

# admin.site.register(Employee)
# admin.site.register(Employee, EmployeeAdmin)
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience_years')
    filter_horizontal = ('services',)