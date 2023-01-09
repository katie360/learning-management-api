from rest_framework import serializers
from .models import AskQuestion, AskQuestionAnswer, Assignment, Curriculum, Resource, ResourceChapter, ResourceTextbook, Subject, Class, TimeTable

class CurriculumSerializer(serializers.ModelSerializer):
   class Meta:
      model = Curriculum
      fields = '__all__'
      
      
class ClassSerializer(serializers.ModelSerializer):
   get_curriculum = serializers.ReadOnlyField()

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

class AssignmentSerializer(serializers.ModelSerializer):
   get_subject = serializers.ReadOnlyField()
   get_teacher = serializers.ReadOnlyField()
   get_file_name = serializers.ReadOnlyField()
   get_file_size = serializers.ReadOnlyField()
   get_formatted_due_date = serializers.ReadOnlyField()

   date_created = serializers.DateTimeField(format='%b %d,%Y %I:%M%p')
   date_due = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

   # Add a field to the serializer
   submitted = serializers.SerializerMethodField()

   def get_submitted(self, obj):
      assignment = obj
      submitted = assignment.submitted
      return submitted


   # def to_representation(self, instance):
   #    data = super().to_representation(instance)
   #    data['submitted'] = self.context.get('submitted')
   #    return data

   class Meta:
      model = Assignment
      fields = '__all__'

class AssignmentDetailSerializer(serializers.ModelSerializer):
   get_subject = serializers.ReadOnlyField()
   get_teacher = serializers.ReadOnlyField()
   get_file_name = serializers.ReadOnlyField()
   get_file_size = serializers.ReadOnlyField()
   get_formatted_due_date = serializers.ReadOnlyField()

   date_created = serializers.DateTimeField(format='%b %d,%Y %I:%M%p')
   date_due = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

   def to_representation(self, instance):
      data = super().to_representation(instance)
      data['submitted'] = self.context.get('submitted')
      data['score'] = self.context.get('score')
      data['date_submitted'] = self.context.get('date_submitted')
      data['comment'] = self.context.get('comment')
      data['uploaded_file'] = self.context.get('uploaded_file')
      return data

   class Meta:
      model = Assignment
      fields = '__all__'
   
