from dataclasses import field
from rest_framework import serializers
from .models import Account
from django.contrib.auth import authenticate


class AccountSerializer(serializers.ModelSerializer):
   class Meta:
      model = Account
      fields = '__all__'
      

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')
