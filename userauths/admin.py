from django.contrib import admin
from userauths.models import User

# Register your models here.
class UserCustomAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']
    

admin.site.register(User, UserCustomAdmin)
