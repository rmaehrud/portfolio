from rest_framework import serializers
from .models import PortfolioList
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')





class PortfolioSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = PortfolioList
        fields = (
            'id',
            'user',
            'title',
            'subtitle',
            'content',
            'bigimage',
            'smallimage',
            'link'
        )

