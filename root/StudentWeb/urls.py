from django.urls import path

from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_student', TemplateView.as_view(template_name='StudentWeb/add_student.html'), name='add_student'),
    path('/post_add_student', views.add_student, name='post_add_student'),
    path('add_course', TemplateView.as_view(template_name='StudentWeb/add_course.html'), name='add_student'),
    path('/post_add_course', views.add_course, name='post_add_course'),
    path('subscribe_courses', views.get_all_list, name='subscribe_courses'),
    path('/post_subscribe_courses', views.subscribe_courses, name='post_subscribe_courses'),

]