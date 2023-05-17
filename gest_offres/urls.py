from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OffreArchiveViewSet, ReservationViewSet, AppreciationViewSet, OffreViewSet, CommentaireViewSet

router = DefaultRouter()
router.register(r'reservations', ReservationViewSet)
router.register(r'appreciations', AppreciationViewSet)
router.register(r'offres', OffreViewSet)
router.register(r'offres-archive', OffreArchiveViewSet)
router.register(r'commentaires', CommentaireViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
