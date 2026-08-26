from django.urls import path
from . import views

app_name = "studentform"

urlpatterns = [
    path("create_students/", views.create_students, name="create_students"),
    path("read_students/", views.read_students, name="read_students"),
    path("student_details/<int:pk>/", views.student_details, name="student_details"),
    path("update_students/<int:pk>", views.update_students, name="update_students"),
    path("student_delete/<int:pk>", views.student_delete, name="student_delete"),
]
