from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)

