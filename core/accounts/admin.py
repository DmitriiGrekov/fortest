from django.contrib import admin
from .models import AdvUser


@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'current_subject')

