from django.urls import path

from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_student', TemplateView.as_view(template_name='StudentWeb/add_student.html'), name='add_student'),
    path('/post_add_student', views.add_student, name='post_add_student'),
]