from rest_framework import serializers
from account.serializers import UserSerializer
from messagerie.models import Message


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(read_only=True)
    recipient = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    # content = serializers.CharField(max_length=None)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'sent_at', 'content']
        
    def create(self, validate_data):
        return Message.objects.save(**validate_data)



class UserMessageSerializer(serializers.Serializer):
    user = UserSerializer()
    last_message = MessageSerializer
    
    
    
    
