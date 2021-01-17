from django.contrib import admin
from app_manage.models import Project, Module


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "describe", "status", "create_time"]


class ModuleAdmin(admin.ModelAdmin):
    list_display = ["name", "describe", "project", "create_time"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)






















