from django.urls import path

from authentification.views import UserLoginView


urlpatterns = [
    path('login/', UserLoginView.as_view())
]
