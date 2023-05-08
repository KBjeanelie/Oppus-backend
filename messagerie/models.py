from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Message(models.Model):
    
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    
    content = models.TextField()
    
    sent_at = models.DateTimeField(auto_now_add=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)



