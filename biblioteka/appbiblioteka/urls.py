from django.urls import path 
from .views import site_knigi, site_clenovi, edna_kniga, eden_clen, pozajmi, vrati

urlpatterns = [
    path("site-knigi", site_knigi),
    path("site-clenovi", site_clenovi),
    path("edna-kniga/", edna_kniga),
    path("eden-clen/", eden_clen),
    path("pozajmi-kniga", pozajmi),
    path("vrati-kniga", vrati)
]
      