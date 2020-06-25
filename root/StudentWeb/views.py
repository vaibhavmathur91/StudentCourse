from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Student, Course, StudentCourses


def get_all_students():
    return Student.objects.all()


def get_all_courses():
    return Course.objects.all()


def get_all_subscription():
    return StudentCourses.objects.all()


def get_all_context():
    students = get_all_students()
    courses = get_all_courses()
    subscriptions = get_all_subscription()
    context = {
        'students_list': students,
        'course_list': courses,
        'subscription_list': subscriptions
    }
    return context


def index(request):
    context = get_all_context()
    return render(request, 'StudentWeb/index.html', context)


def add_student(request):
    f_name = request.POST["first_name"]
    l_name = request.POST["last_name"]
    dob = request.POST["date_of_birth"]
    phone = request.POST["number"]
    print(request, request.POST)
    Student(
        first_name=f_name,
        last_name=l_name,
        birth_date=dob,
        contact_number=phone
    ).save()
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


def get_all_list(request):
    context = get_all_context()
    return render(request, 'StudentWeb/subscribe_courses.html', context)


def subscribe_courses(request):
    print(request, request.POST)
    request_student = Student.objects.get(id=int(request.POST["student"]))
    request_course = Course.objects.get(id=int(request.POST["course"]))
    print(request_student, request_course)
    StudentCourses(
        student=request_student,
        course=request_course,
    ).save()
    return HttpResponseRedirect("/")
