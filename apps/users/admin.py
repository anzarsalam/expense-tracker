from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    pass
