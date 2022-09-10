"""
Admin customisation
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as T

from core import models


class UserAdmin(BaseUserAdmin):
    """ Define admin pages for user """

    ordering = ['id']
    list_display= ['email', 'name', 'is_staff', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name',)}),
        (
            T('Permissions'),
            {
                'fields':(
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (T('Important Dates'), {'fields': ('last_login',)}),
    )
    readonly_fields =['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Product)

