from django.contrib import admin
from workers.models import Employee, JobPosition

# Register your models here.
admin.site.register(Employee)
admin.site.register(JobPosition)
