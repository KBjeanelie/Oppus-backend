from django.urls import include, path
from rest_framework import routers
from .views import EmployeurViewSet,WorkerViewSet

router = routers.DefaultRouter()
router.register(r'workers', WorkerViewSet)
router.register(r'employeurs', EmployeurViewSet)
urlpatterns = [
    path('', include(router.urls))
]
