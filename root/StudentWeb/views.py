from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Course, StudentCourses


def get_all_students():
    return Student.objects.all()


def index(request):
    students = get_all_students()
    context = {
        'students_list': students,
    }
    return render(request, 'StudentWeb/index.html', context)


def add_student(request):
    f_name = request.POST("first_name")
    l_name = request.POST("last_name")
    dob = request.POST("date_of_birth")
    phone = request.POST("number")

    student = Student(
        first_name=f_name,
        last_name=l_name,
        birth_date=dob,
        contact_number=phone
    ).save()

    return get_all_students()
