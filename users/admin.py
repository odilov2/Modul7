
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Users


@admin.register(Users)
class UsersAdmin(ImportExportModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'username']
    search_fields = ['first_name']
    ordering = ['id']
