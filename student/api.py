from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from student.models import StudentTakesCourse
from student.serializers import StudentCourseSerializer

from student.permissions import IsStudentUser

class StudentCoursesList(APIView):
    '''
        Get all the courses that the logged in student is enrolled in

        *Requires Token Authorization
        *Only student users to be able to get information from this API call
    '''

    authentication_classes= [authentication.TokenAuthentication]
    permission_classes= [permissions.IsAuthenticated, IsStudentUser]

    def get(self, request, format= None):
        '''
            Returns Courses enrolled in by the student
        '''
        student_takes_courses= StudentTakesCourse.objects.filter(student__user= request.user)
        serializer= StudentCourseSerializer(student_takes_courses, many= True)
        return Response(serializer.data)