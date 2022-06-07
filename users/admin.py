from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','phone','name', 'is_staff', 'is_active',)
    list_filter = ('email','phone','name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email','phone','name','pfp', 'password')}),
        ('Permissions', {'fields': ('is_blog','is_team', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','phone','name', 'pfp','password1', 'password2','is_blog','is_team', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
