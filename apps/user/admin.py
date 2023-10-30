from django.contrib import admin
from apps.user.models.user_model import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models.rol_model import Rol

# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': (
            'email', 'password', 'last_name', 'is_active', 'is_staff', 'is_superuser',
            'groups',
            'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Rol para instituciones', {'fields': ('rol',)}),
    )

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Tipos', {'fields': ('type',)}),
    )
