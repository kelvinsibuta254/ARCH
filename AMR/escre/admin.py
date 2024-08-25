from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from .models import Staff
# Register your models here.
class UserAdmin(CustomUserAdmin):
    list_display = ("email", "is_staff")

admin.site.register(Staff, UserAdmin)