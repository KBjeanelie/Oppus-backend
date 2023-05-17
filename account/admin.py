from django.contrib import admin
from account.models import Employeur, Gestionnaire, User, Worker
from gest_qual_ouvrier.models import Competence

# Register your models here.
admin.site.register(User)
admin.site.register(Worker)
admin.site.register(Gestionnaire)
admin.site.register(Employeur)
admin.site.register(Competence)