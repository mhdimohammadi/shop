from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ShopUserChangeForm, ShopUserCreationForm
from .models import ShopUser


@admin.register(ShopUser)
class ShopUserAdmin(UserAdmin):
    ordering = ['phone']
    add_form = ShopUserCreationForm
    form = ShopUserChangeForm
    model = ShopUser
    list_display = ['phone', 'first_name', 'last_name', 'is_active', 'is_staff']
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('personal info', {'fields': ('first_name', 'last_name', 'address')}),
        ('permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('important dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {'fields': ('phone', 'password1', 'password2')}),
        ('personal info', {'fields': ('first_name', 'last_name', 'address')}),
        ('permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('important dates', {'fields': ('last_login', 'date_joined')})
    )
