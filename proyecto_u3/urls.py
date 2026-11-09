from django.contrib import admin
from django.urls import path

from mascotas.views import crear_mascota, listar_mascotas, modificar_mascotas, eliminar_mascotas
from mascotas.views import crear_responsable, listar_responsable, modificar_responsable, eliminar_responsable

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mascota/crear', crear_mascota),
    path('mascotas', listar_mascotas),
    path('mascota/modificar/<int:id>', modificar_mascotas),
    path('mascota/eliminar/<int:id>', eliminar_mascotas),

    path('responsable/crear', crear_responsable),
    path('responsables', listar_responsable),
    path('responsable/modificar/<int:id>', modificar_responsable),
    path('responsable/eliminar/<int:id>', eliminar_responsable),
]
