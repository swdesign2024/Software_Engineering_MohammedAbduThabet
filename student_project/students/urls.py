from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("students/", views.all_students, name="all_students"),
    path("students/<int:student_id>/", views.student_detail, name="student_detail"),
    path("add/", views.add_student, name="add_student"),
]
