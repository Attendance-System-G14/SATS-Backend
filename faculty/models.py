from django.db import models
from django.contrib.auth.models import User
from course.models import Department, Course

# Create your models here.

class Faculty(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.__str__()

class FacultyTakesCourse(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("faculty", "course"),)


    def __str__(self):
        return self.course.__str__() + ' '  + self.faculty.__str__()  
