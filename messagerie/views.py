from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from messagerie.models import Message
from messagerie.serializers import MessageSerializer, UserMessageSerializer
from django.db.models import Q, Max
from messagerie.serializers import UserSerializer



User = get_user_model()


class MessagesListView(APIView):

    def get(self, request, sender_id, recipient_id):
        try:
            sender = User.objects.get(id=sender_id)
            recipient = User.objects.get(id=recipient_id)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        messages = Message.objects.filter(sender=sender, recipient=recipient).order_by('sent_at') | Message.objects.filter(sender=recipient, recipient=sender).order_by('sent_at')
        messages_serialized = MessageSerializer(messages, many=True)
        return Response(messages_serialized.data)



class UserMessagesListView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # récupérer la liste de tous les utilisateurs avec lesquels l'utilisateur a discuté
        sender_qs = Message.objects.filter(recipient=user).values('sender').distinct()
        recipient_qs = Message.objects.filter(sender=user).values('recipient').distinct()
        users_qs = sender_qs.union(recipient_qs)
        users = User.objects.filter(id__in=users_qs)
        
        # récupérer le dernier message de chaque discussion
        messages = []
        for other_user in users:
            last_message = Message.objects.filter(Q(sender=user, recipient=other_user) | Q(sender=other_user, recipient=user)).order_by('-sent_at').first()
            if last_message:
                messages.append({
                    'user_id': UserSerializer(other_user).data,
                    'last_message': MessageSerializer(last_message).data
                })

        return Response(messages)
    






































    # Récupération des utilisateurs ayant envoyé un message à l'utilisateur 5 ou à qui l'utilisateur 5 a envoyé un message
    # users = User.objects.filter(Q(sent_messages__recipient_id=user_id) | Q(received_messages__sender_id=user_id)).distinct()
    
    # discussions = []
    
    # for user in users:
    #     # Récupération du dernier message entre l'utilisateur 5 et l'utilisateur courant
    #     last_message = Message.objects.filter((Q(sender_id=user_id) & Q(recipient_id=user.id)) | (Q(sender_id=user.id) & Q(recipient_id=user_id))).order_by('-sent_at').first()
    #     if last_message:
    #         # Sérialisation de l'utilisateur et du dernier message
    #         discussion = {'user': UserSerializer(user).data, 'last_message': MessageSerializer(last_message).data}
    #         discussions.append(discussion)

    # return Response({'discussions': discussions})
