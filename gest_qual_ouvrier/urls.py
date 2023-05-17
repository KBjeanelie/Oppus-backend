from django.urls import path, include
from rest_framework import routers
from .views import CompetenceViewSet, FormationViewSet, ExperienceViewSet

router = routers.DefaultRouter()
router.register(r'competences', CompetenceViewSet)
#router.register(r'etablissements', EtablissementViewSet)
#router.register(r'diplomes', DiplomeViewSet)
#router.register(r'domaines_etude', Domaine_EtudeViewSet)
router.register(r'formations', FormationViewSet)
router.register(r'experiences', ExperienceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
