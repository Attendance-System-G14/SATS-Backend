from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    entry_number = models.CharField(max_length=20)
    department = models.ForeignKey('course.Department', null=True, on_delete=models.SET_NULL)

class StudentTakesCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE)
