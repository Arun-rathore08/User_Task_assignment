from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import User, Task



class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("name", "email", "mobile", "Id", "task")
    
class TaskAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("task_details", "task_type")

admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)