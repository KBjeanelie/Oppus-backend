from django.urls import path

from authentification.views import EmployeurLoginView, EmployeurRegisterView, GetCurrentEmployeur, UserLogoutView, WorkerRegisterView


urlpatterns = [
    path('login/', EmployeurLoginView.as_view()),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('employeur/register/', EmployeurRegisterView.as_view()),
    path('employeur/get-current-user/', GetCurrentEmployeur.as_view()),
    path('worker/register/', WorkerRegisterView.as_view())
]
