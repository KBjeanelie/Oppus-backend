from django.contrib import admin
from account.models import Employeur, Gestionnaire, User, Worker

# Register your models here.
admin.site.register(User)
admin.site.register(Worker)
admin.site.register(Gestionnaire)
admin.site.register(Employeur)