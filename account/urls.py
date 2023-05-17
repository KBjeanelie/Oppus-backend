from django.urls import include, path
from account.views import EmployeurRegistrationView, GetCurrentUserView, UserLoginView, WorkerRegistrationView
from rest_framework import routers
from .views import EmployeurViewSet, WorkerViewSet

router = routers.DefaultRouter()
router.register(r'workers', WorkerViewSet)
router.register(r'employeurs', EmployeurViewSet)
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('employeur/register/', EmployeurRegistrationView.as_view(), name='employeur-register'),
    path('worker/register/', WorkerRegistrationView.as_view(), name='worker-register'),
    path('get_current_user/', GetCurrentUserView.as_view()),
    path('', include(router.urls))
]
