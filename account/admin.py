from django.contrib import admin
from account.models import Employeur, Gestionnaire, User, Ouvrier
from gest_qual_ouvrier.models import Competence

# Register your models here.
admin.site.register(User)
admin.site.register(Ouvrier)
admin.site.register(Gestionnaire)
admin.site.register(Employeur)
admin.site.register(Competence)