import json
from django.shortcuts import render
from rest_framework import viewsets, status

from curriculum.models import Exam, StudentAnnouncement, TimeTable
from curriculum.serializers import AskQuestionSerializer, SubjectSerializer, TimeTableSerializer
from .models import Student
from .serializers import StudentAnnouncementSerializer, StudentExamSerializer, StudentSerializer
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import generics, permissions, serializers
from knox.models import AuthToken
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse, HttpResponse


from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView



class StudentViewSet(viewsets.ModelViewSet):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer


@api_view(['GET'])
def get_student_data(request):
    user = request.user

    if user.is_authenticated:
        student = Student.objects.get(user=user)
        return Response({
            'student_info': {
                'id': student.id,
                'username': student.username,
                'contact_no': student.contact_no,
                'parent_name': student.parent_name,
                'parent_phone_no': student.parent_phone_no,
                'city': student.city,
                'country': student.country,
                'profile_image': student.profile.url,
                'about': student.about,
            },
        })
    else:
        return Response('User is not authenticated', status=401)


@api_view(['GET'])
def get_subjects_enrolled(request):
    user = request.user

    if user.is_authenticated:
        student = Student.objects.get(user=user)
        subjects = student.subject.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)
    else:
        return Response('User is not authenticated', status=401)

@api_view(['GET'])
def get_student_timetable(request):
    user = request.user

    if user.is_authenticated:
        student = Student.objects.get(user=user)
        timetables = TimeTable.objects.all()
        
        print(timetables)
        subjects = student.subject.all()
        print(subjects)

        timetable_result = []
        if timetables.count() > 0:
            for subject in subjects:
                for timetable in timetables:
                    if timetable.subject == subject:
                        print(timetable)
                        group = timetable.subject.subject_class.name
                        timetable_result.append({"day":timetable.day, "subject":timetable.subject.name, "from":timetable.start_time.strftime("%I:%M%p"), "to":timetable.end_time.strftime("%I:%M%p"), "venue":timetable.link, "group":group, "teacher":timetable.teacher.user.first_name + " " + timetable.teacher.user.last_name})
                print(timetable_result)
            return JsonResponse({'timetable': list(timetable_result)})
            # timetables_serializer = TimeTableSerializer(timetable_result, many=True)
            # return Response({'timetable': timetables_serializer.data})
            # return JsonResponse(timetable_result)
                        # print(timetable)
                        # return JsonResponse({'timetable': list(timetable)})
        else:
            return JsonResponse({'timetable': 'No timetable found'})
    else:
        return Response('User is not authenticated', status=401)

@api_view(['GET'])
def get_student_announcements(request):
    user = request.user

    if user.is_authenticated:
        student = Student.objects.get(user=user)
        announcements = StudentAnnouncement.objects.all()
        serializer = StudentAnnouncementSerializer(announcements, many=True)
        return Response(serializer.data)
    else:
        return Response('User is not authenticated', status=401)


@api_view(['GET'])
def get_student_announcement_detail(request, id):
    user = request.user

    if user.is_authenticated:
        announcement = StudentAnnouncement.objects.get(id=id)
        serializer = StudentAnnouncementSerializer(announcement)
        return Response(serializer.data)
    else:
        return Response('User is not authenticated', status=401)


@api_view(['GET'])
def get_student_exams(request):
    user = request.user

    if user.is_authenticated:
        student = Student.objects.get(user=user)
        exams = Exam.objects.filter(subject__in = student.subject.all())
        serializer = StudentExamSerializer(exams, many=True)
        return Response(serializer.data)
    else:
        return Response('User is not authenticated', status=401)

@api_view(['POST'])
def student_ask_question(request):
    user = request.user

    if user.is_authenticated:
        student = Student.objects.get(user=user)
        question = request.data['question']
        created_by = student.id
        data = {'question': question, 'created_by': created_by}
        print(question)
        # save question to database table ask_question
        serializer = AskQuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('Question asked successfully', status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response('Question not asked', status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response('User is not authenticated', status=401)

