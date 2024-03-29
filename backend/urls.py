"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Oppuss-Backend API')

urlpatterns = [
    re_path(r'^$', schema_view),
    path('admin/', admin.site.urls),
    path('', include('messagerie.urls')),
    path('api/auth/', include('authentification.urls')),
    path('api/gestion/compte/', include('account.urls')),
    path('api/referentiel-btp/', include('ref_dom_btp.urls')),
    path('api/gestion/messagerie/', include('messagerie.urls')),
    path('api/gestion/qualification-ouvrier/', include('gest_qual_ouvrier.urls')),
    path('api/gestion/offres/', include('gest_offres.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
