from django.contrib import admin

from ref_dom_btp.models import Domaine, Metier, Travaux

# Register your models here.

admin.site.register(Domaine)
admin.site.register(Travaux)
admin.site.register(Metier)