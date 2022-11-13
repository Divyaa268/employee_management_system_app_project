from django.contrib import admin
from .models import Employee, Role, Department,CEO,BestPerformers
# Register your models here.

admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(CEO)
admin.site.register(BestPerformers)

