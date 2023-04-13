from django.urls import path
from account.views import GetCurrentUserView, UserLoginView, UserRegistrationClientView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register-client/', UserRegistrationClientView.as_view(), name='register-client'),
    path('get_current_user/', GetCurrentUserView.as_view())
]
