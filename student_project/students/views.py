# ====== students/views.py ======
from django.shortcuts import render

# بيانات الطلاب (بدون قاعدة بيانات)
students_data = [
    {
        "FirstName": "أحمد",
        "LastName": "الهاشمي",
        "Age": 21,
        "Gender": "ذكر",
        "Level": "السنة الثالثة",
        "Status": "نعم",
    },
    {
        "FirstName": "محمد",
        "LastName": "الحضرمي",
        "Age": 22,
        "Gender": "ذكر",
        "Level": "السنة الرابعة",
        "Status": "نعم",
    },
    {
        "FirstName": "ليلى",
        "LastName": "الشريف",
        "Age": 19,
        "Gender": "أنثى",
        "Level": "السنة الأولى",
        "Status": "نعم",
    },
    {
        "FirstName": "فهد",
        "LastName": "القاسمي",
        "Age": 23,
        "Gender": "ذكر",
        "Level": "السنة الخامسة",
        "Status": "لا",
    },
    {
        "FirstName": "سارة",
        "LastName": "الزهري",
        "Age": 20,
        "Gender": "أنثى",
        "Level": "السنة الثانية",
        "Status": "نعم",
    },
    {
        "FirstName": "عبدالله",
        "LastName": "النعيمي",
        "Age": 24,
        "Gender": "ذكر",
        "Level": "السنة الخامسة",
        "Status": "لا",
    },
    {
        "FirstName": "مريم",
        "LastName": "العسيري",
        "Age": 18,
        "Gender": "أنثى",
        "Level": "السنة الأولى",
        "Status": "نعم",
    },
    {
        "FirstName": "خالد",
        "LastName": "المري",
        "Age": 22,
        "Gender": "ذكر",
        "Level": "السنة الرابعة",
        "Status": "نعم",
    },
    {
        "FirstName": "هدى",
        "LastName": "القرشي",
        "Age": 21,
        "Gender": "أنثى",
        "Level": "السنة الثالثة",
        "Status": "نعم",
    },
    {
        "FirstName": "بدر",
        "LastName": "التميمي",
        "Age": 23,
        "Gender": "ذكر",
        "Level": "السنة الخامسة",
        "Status": "لا",
    },
]


def home(request):
    return render(request, "home.html")


def all_students(request):
    return render(request, "all_students.html", {"students": students_data})


def student_detail(request, student_id):
    if 0 <= student_id < len(students_data):
        student = students_data[student_id]
    else:
        student = None
    return render(request, "student_detail.html", {"student": student})


def add_student(request):
    return render(request, "add_student.html")
