import datetime
from django.contrib.auth.models import User
from rest_framework import serializers
from chat_api.models import Message


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    timestamp = serializers.DateTimeField(default=datetime.datetime.now())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']

