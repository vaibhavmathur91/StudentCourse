from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Student, Course, StudentCourses


def get_all_students():
    return Student.objects.all()


def get_all_courses():
    return Course.objects.all()


def index(request):
    students = get_all_students()
    courses = get_all_courses()
    context = {
        'students_list': students,
        'course_list': courses,
    }
    return render(request, 'StudentWeb/index.html', context)


def add_student(request):
    f_name = request.POST["first_name"]
    l_name = request.POST["last_name"]
    dob = request.POST["date_of_birth"]
    phone = request.POST["number"]
    print(request, request.POST)
    # Student(
    #     first_name=f_name,
    #     last_name=l_name,
    #     birth_date=dob,
    #     contact_number=phone
    # ).save()
    return HttpResponseRedirect("/")


def add_course(request):
    req_course_name = request.POST["course_name"]
    req_course_details = request.POST["course_details"]
    print(request, request.POST)
    Course(
        course_name=req_course_name,
        course_details=req_course_details,
    ).save()
    return HttpResponseRedirect("/")
