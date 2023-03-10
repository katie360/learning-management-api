from rest_framework import serializers

from curriculum.models import AskQuestion, Exam, StudentAnnouncement
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

# class SubjectsEnrolledSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'

class StudentAnnouncementSerializer(serializers.ModelSerializer):
    date_created = serializers.DateTimeField(format='%b %d,%Y %I:%M%p')
    class Meta:
        model = StudentAnnouncement
        fields = '__all__'

class StudentExamSerializer(serializers.ModelSerializer):
    get_subject = serializers.ReadOnlyField()
    get_teacher = serializers.ReadOnlyField()
    get_formatted_exam_date = serializers.ReadOnlyField()

    class Meta:
        model = Exam
        fields = '__all__'

class StudentAskQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AskQuestion
        fields = '__all__'
