from django.urls import path

from authentification.views import EmployeurRegisterView, UserLoginView, WorkerRegisterView


urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('employeur/register/', EmployeurRegisterView.as_view()),
    path('worker/register/', WorkerRegisterView.as_view())
]
