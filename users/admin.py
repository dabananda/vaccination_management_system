from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile


class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email', 'role', 'nid']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'role', 'nid')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'role', 'nid', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    filter_horizontal = ()
    list_filter = ()
    username = None


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
