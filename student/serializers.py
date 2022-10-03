from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

# class SubjectsEnrolledSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'
