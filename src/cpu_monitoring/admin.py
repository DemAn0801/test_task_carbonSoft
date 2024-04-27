from django.contrib import admin
from .models import SystemInfo


class SystemInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "cpu_avg", "created")
    search_fields = ("created",)


admin.site.register(SystemInfo, SystemInfoAdmin)
