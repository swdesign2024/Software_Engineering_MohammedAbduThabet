# teachers/views.py

from django.shortcuts import render
from school_project.data import teachers_data


def teacher_list(request):
    return render(request, "teachers/teacher_list.html", {"teachers": teachers_data})


def teacher_detail(request, pk):
    teacher = next((item for item in teachers_data if item["id"] == pk), None)
    return render(request, "teachers/teacher_detail.html", {"teacher": teacher})
