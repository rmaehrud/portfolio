from rest_framework import serializers
from .models import BigData
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')





class BigDataSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = BigData
        fields = (
            'id',
            'user',
            'object_type',
            'text',
            'link',
            'button_title',
        )

