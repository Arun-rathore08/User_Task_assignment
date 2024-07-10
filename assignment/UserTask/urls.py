from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexView, name="index"),
    path("user", views.userView, name="user"),
    path("task/", views.taskView, name="task"),  
    path("user_list/", views.userListView, name="user_list"),
    path("task_list/", views.taskListView, name="task_list"),
    path("export_to_excel/", views.export_to_excel, name="export_to_excel"),   # for exporting data to excel file.
]
