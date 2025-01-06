from django.contrib import admin
from .models import Employee  # Import your Employee model

# Register the Employee model in the admin panel
admin.site.register(Employee)
