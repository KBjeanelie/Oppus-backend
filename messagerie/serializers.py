from rest_framework import serializers
from account.serializers import UserSerializer
from .models import Discussion

class DiscussionSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Discussion
        fields = ['id', 'content', 'sender', 'receiver', 'day', 'time']
        read_only_fields = ['id', 'day', 'time']
