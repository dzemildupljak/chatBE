from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer, MessageSerializer
from .models import Message
# Create your views here.


@api_view(http_method_names=['GET'])
def get_all_users(request):
    """
    Get all users
    """
    all_users = User.objects.all()
    serializer = UserSerializer(all_users, many=True)
    return Response(serializer.data)    


@api_view(http_method_names=['POST'])
def create_messages(request):
    """
    Get all messages
    """
    data = JSONParser().parse(request)
    serializer = MessageSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['GET'])
def get_all_messages(request, sender=None, receiver=None):
    """
    Get all messages
    """
    messages = Message.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)