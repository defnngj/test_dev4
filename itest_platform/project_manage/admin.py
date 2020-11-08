from django.contrib import admin
from project_manage.models import Project, Module
# Register your models here.
# 把models创建的表快速映射到admin后台


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "describe", "status", "create_time"]


class ModuleAdmin(admin.ModelAdmin):
    list_display = ["name", "describe", "project", "create_time"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)
