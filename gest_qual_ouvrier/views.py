from rest_framework import viewsets
from .models import Competence, Formation, Experience
from .serializers import CompetenceSerializer, FormationSerializer, ExperienceSerializer


class CompetenceViewSet(viewsets.ModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer


class FormationViewSet(viewsets.ModelViewSet):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer



# class EtablissementViewSet(viewsets.ModelViewSet):
#     queryset = Etablissement.objects.all()
#     serializer_class = EtablissementSerializer


# class DiplomeViewSet(viewsets.ModelViewSet):
#     queryset = Diplome.objects.all()
#     serializer_class = DiplomeSerializer


# class Domaine_EtudeViewSet(viewsets.ModelViewSet):
#     queryset = Domaine_Etude.objects.all()
#     serializer_class = DomaineEtudeSerializer

