import imp
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AskQuestion, Class, Curriculum, Resource, ResourceChapter, ResourceTextbook, Subject
from .serializers import  AskQuestionSerializer, ClassSerializer, CurriculumSerializer, ResourceChapterSerializer, ResourceSerializer, ResourceTextbookSerializer, SubjectSerializer


class CurriculumViewSet(viewsets.ModelViewSet):
   queryset = Curriculum.objects.all()
   serializer_class = CurriculumSerializer

   
class ClassViewSet(viewsets.ModelViewSet):
   queryset = Class.objects.all()
   serializer_class = ClassSerializer
   
class SubjectViewSet(viewsets.ModelViewSet):
   queryset = Subject.objects.all()
   serializer_class = SubjectSerializer

class ResourceViewSet(viewsets.ModelViewSet):
   queryset = Resource.objects.all()
   serializer_class = ResourceSerializer

class ResourceChapterViewSet(viewsets.ModelViewSet):
   queryset = ResourceChapter.objects.all()
   serializer_class = ResourceChapterSerializer
   
@api_view(['GET'])
def get_curriculum(request):
   curriculum = Curriculum.objects.all()
   serializer = CurriculumSerializer(curriculum, many=True)
   return Response(serializer.data)

@api_view(['GET'])
def get_resources(request):
   resources = Resource.objects.all()
   serializer = ResourceSerializer(resources, many=True)
   
   return Response(serializer.data)

@api_view(['GET'])
def get_resource_chapters(request, pk):
   resource_chapters = ResourceChapter.objects.filter(resource_id=pk)
   # chapters = resource.chapters.all()
   serializer = ResourceChapterSerializer(resource_chapters, many=True)
   
   # if data is empty, return null
   if not serializer.data:
      return Response("null")
   return Response(serializer.data)

@api_view(['GET'])
def get_single_resource_chapter(request, pk):
   resource_chapter = ResourceChapter.objects.get(id=pk)
   serializer = ResourceChapterSerializer(resource_chapter, many=False)
   return Response(serializer.data)

@api_view(['GET'])
def get_resource_textbooks_free(request):
   resource_textbooks = ResourceTextbook.objects.filter(free = True)
   serializer = ResourceTextbookSerializer(resource_textbooks, many=True)
   return Response(serializer.data)

@api_view(['GET'])
def get_resource_textbooks_paid(request):
   resource_textbooks = ResourceTextbook.objects.filter(free = False)
   serializer = ResourceTextbookSerializer(resource_textbooks, many=True)
   return Response(serializer.data)

@api_view(['GET', 'POST'])
def get_asked_questions(request):
   if request.method == 'GET':
      asked_questions = AskQuestion.objects.all()
      serializer = AskQuestionSerializer(asked_questions, many=True)
      return Response(serializer.data)
   elif request.method == 'POST':
      serializer = AskQuestionSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
      return Response(serializer.data)


