from django.contrib import admin
from .models import Student

class StudentCustomAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age']

admin.site.register(Student, StudentCustomAdmin)