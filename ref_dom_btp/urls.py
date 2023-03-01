from django.urls import path, include
from rest_framework import routers
from .views import DomaineViewSet, MetierViewSet, TravauxViewSet

router = routers.DefaultRouter()
router.register(r'domaines', DomaineViewSet)
router.register(r'travaux', TravauxViewSet)
router.register(r'metier', MetierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]