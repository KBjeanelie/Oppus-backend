from django.contrib import admin

from gest_qual_ouvrier.models import Diplome, Domaine_Etude, Etablissement, Formation, Experience

# Register your models here.
admin.site.register(Etablissement)
admin.site.register(Diplome)
admin.site.register(Domaine_Etude)
admin.site.register(Formation)
admin.site.register(Experience)