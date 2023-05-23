from django.db import models

from account.models import User


class Discussion(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(User, related_name='sender_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='message_receiver', on_delete=models.CASCADE)
    day = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"Message : {self.content}"