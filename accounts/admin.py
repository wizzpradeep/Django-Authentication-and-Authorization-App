from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, EmailVerification

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['id', 'first_name', 'last_name', 'username', 'email', 'is_active', 'is_staff', 'date_joined']

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )

    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('username',)


class EmailVerificationAdmin(admin.ModelAdmin):
    list_display =['id', 'user','token','is_verified']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(EmailVerification, EmailVerificationAdmin)

