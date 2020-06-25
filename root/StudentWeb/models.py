from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    contact_number = models.CharField(max_length=15)


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_details = models.CharField(max_length=200)


class StudentCourses(models.Model):
    class Meta:
        unique_together = ['student', 'course']
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
