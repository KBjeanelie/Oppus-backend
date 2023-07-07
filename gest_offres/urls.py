from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GetWorkerByOfferAPIView, OffreArchiveViewSet, ReservationViewSet, AppreciationViewSet, OffreViewSet, CommentaireViewSet

router = DefaultRouter()
router.register(r'reservations', ReservationViewSet)
router.register(r'appreciations', AppreciationViewSet)
router.register(r'offres', OffreViewSet, basename='offre')
router.register(r'offres-archive', OffreArchiveViewSet, basename='offre-archive')
router.register(r'commentaires', CommentaireViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:offre_id>/workers/', GetWorkerByOfferAPIView.as_view(), name='worker-by-travaux'),
]
