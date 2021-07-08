from django.contrib import admin
# Register your models here.
from aplicacion.models import periodista
from aplicacion.models import medio
from aplicacion.models import tipo_medio
from aplicacion.models import publicacion
from aplicacion.models import competencia
from aplicacion.models import posee




admin.site.register(periodista)
admin.site.register(medio)
admin.site.register(tipo_medio)
admin.site.register(publicacion)
admin.site.register(competencia)
admin.site.register(posee)

