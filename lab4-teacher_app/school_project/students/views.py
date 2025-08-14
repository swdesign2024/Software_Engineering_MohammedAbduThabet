# students/views.py

from django.shortcuts import render
from school_project.data import students_data


def student_list(request):
    return render(request, "students/student_list.html", {"students": students_data})


def student_detail(request, pk):
    student = next((item for item in students_data if item["id"] == pk), None)
    return render(request, "students/student_detail.html", {"student": student})
