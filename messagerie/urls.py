from django.urls import path
from .views import MessagesListView, SendMessage, UserMessagesListView

urlpatterns = [
    path('new_messages/', SendMessage.as_view(), name='send_message'),
    path('messages/<int:user_id>/', UserMessagesListView.as_view(), name='user-message-list'),
    path('messages/<int:sender_id>/<int:recipient_id>/', MessagesListView.as_view(), name='message-list'),
]