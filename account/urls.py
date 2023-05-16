from django.urls import path
from account.views import EmployeurRegistrationView, GetCurrentUserView, UserLoginView, UserRegistrationClientView, WorkerRegistrationView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('employeur/register/', EmployeurRegistrationView.as_view(), name='employeur-register'),
    path('worker/register/', WorkerRegistrationView.as_view(), name='worker-register'),
    path('get_current_user/', GetCurrentUserView.as_view())
]
