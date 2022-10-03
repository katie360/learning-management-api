from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from LMS.constants import SCHOOL_NAME
from student.serializers import StudentSerializer
from .models import Manager
from .serializers import ManagerSerializer
from student.models import Student
from teacher.models import Teacher
from curriculum.models import Curriculum, Class, Subject, Resource

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

def getLoggedInManager(user_id):
    s = Manager.objects.get(user_id=user_id)
    return s 


@api_view(['GET'])
def ManagerDashboard(request):
    user_id = request.user.id
    manager = getLoggedInManager(2)
    students_count = Student.objects.count()
    teachers_count = Teacher.objects.count()
    subjects_count = Subject.objects.count()
    classes_count = Class.objects.count()
    manager_serializer = ManagerSerializer(manager)
    student_serializer = StudentSerializer(students_count)
    context = {
        'manager': manager_serializer.data,
        # 'students_count': student_serializer.data,
    }
    return Response(context, status=status.HTTP_200_OK)

