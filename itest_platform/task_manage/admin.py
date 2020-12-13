from django.contrib import admin
from task_manage.models import Task, TaskCase


class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "status", "create_time"]


class TaskCaseAdmin(admin.ModelAdmin):
    list_display = ["task", "case", "create_time"]


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskCase, TaskCaseAdmin)
