from django.contrib import admin

from gest_offres.models import Appreciation, Commentaire, Offre, Reservation

# Register your models here.
admin.site.register(Commentaire)
admin.site.register(Reservation)
admin.site.register(Appreciation)
admin.site.register(Offre)