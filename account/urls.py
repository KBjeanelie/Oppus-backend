from django.urls import include, path
from account.views import EmployeurRegistrationView, UserLoginView, WorkerRegistrationView
from rest_framework import routers
from .views import EmployeurViewSet, GetCurrentEmployeurView, GetCurrentWorkerView, WorkerViewSet

router = routers.DefaultRouter()
router.register(r'workers', WorkerViewSet)
router.register(r'employeurs', EmployeurViewSet)
urlpatterns = [
    path('employeur/register/', EmployeurRegistrationView.as_view(), name='employeur-register'),
    path('employeur/get_current_user/', GetCurrentEmployeurView.as_view()),
    path('worker/register/', WorkerRegistrationView.as_view(), name='worker-register'),
    path('worker/get_current_user/', GetCurrentWorkerView.as_view()),
    path('login/', UserLoginView.as_view(), name='login'),
    path('', include(router.urls))
]
