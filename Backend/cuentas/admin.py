from django.contrib import admin
from .models import Perfiles, Comentarios, Categorias, Publicaciones

# Registrar los modelos.

admin.site.register(Perfiles)
admin.site.register(Comentarios)
admin.site.register(Categorias)
admin.site.register(Publicaciones)