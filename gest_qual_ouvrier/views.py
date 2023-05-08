from rest_framework import viewsets
from rest_framework.response import Response
from .models import Competence, Etablissement, Diplome, Domaine_Etude, Formation, Experience, Competence_Ouvrier
from .serializers import CompetenceOuvrierSerializer, CompetenceSerializer, DomaineEtudeSerializer, EtablissementSerializer, DiplomeSerializer, FormationSerializer, ExperienceSerializer


class CompetenceViewSet(viewsets.ModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer


class EtablissementViewSet(viewsets.ModelViewSet):
    queryset = Etablissement.objects.all()
    serializer_class = EtablissementSerializer


class DiplomeViewSet(viewsets.ModelViewSet):
    queryset = Diplome.objects.all()
    serializer_class = DiplomeSerializer


class Domaine_EtudeViewSet(viewsets.ModelViewSet):
    queryset = Domaine_Etude.objects.all()
    serializer_class = DomaineEtudeSerializer


class FormationViewSet(viewsets.ModelViewSet):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class Competence_OuvrierViewSet(viewsets.ModelViewSet):
    queryset = Competence_Ouvrier.objects.all()
    serializer_class = CompetenceOuvrierSerializer
