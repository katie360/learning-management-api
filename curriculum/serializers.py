from rest_framework import serializers
from .models import AskQuestion, AskQuestionAnswer, Curriculum, Resource, ResourceChapter, ResourceTextbook, Subject, Class, TimeTable

class CurriculumSerializer(serializers.ModelSerializer):
   class Meta:
      model = Curriculum
      fields = '__all__'
      
      
class ClassSerializer(serializers.ModelSerializer):
   class Meta:
      model = Class
      fields = '__all__'
      
class SubjectSerializer(serializers.ModelSerializer):
   class Meta:
      model = Subject
      fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
   get_subject = serializers.ReadOnlyField()
   class Meta:
      model = Resource
      fields = '__all__'

class ResourceChapterSerializer(serializers.ModelSerializer):
   get_resource = serializers.ReadOnlyField()
   class Meta:
      model = ResourceChapter
      fields = '__all__'

class ResourceTextbookSerializer(serializers.ModelSerializer):
   get_subject = serializers.ReadOnlyField()
   class Meta:
      model = ResourceTextbook
      fields = '__all__'
      
class AskQuestionSerializer(serializers.ModelSerializer):
   class Meta:
      model = AskQuestion
      fields = '__all__'

class AskQuestionAnswerSerializer(serializers.ModelSerializer):
   class Meta:
      model = AskQuestionAnswer
      fields = '__all__'


class TimeTableSerializer(serializers.ModelSerializer):
   get_subject = serializers.ReadOnlyField()
   get_teacher = serializers.ReadOnlyField()
   get_class = serializers.ReadOnlyField()

   start_time = serializers.DateTimeField(format='%I:%M%p')
   end_time = serializers.DateTimeField(format='%I:%M%p')
   class Meta:
      model = TimeTable
      fields = '__all__'