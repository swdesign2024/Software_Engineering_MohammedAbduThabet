# teachers/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.teacher_list, name="teacher_list"),
    path("details/<int:pk>/", views.teacher_detail, name="teacher_detail"),
]
