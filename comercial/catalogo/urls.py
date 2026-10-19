from django.urls import path
from .views.categoria import lista_categorias, agregar_categoria, eliminar_categoria

urlpatterns = [
    path("categoria/", lista_categorias, name="list_categoria"),
    path("categoria/agregar/", agregar_categoria, name="agregar_categoria"),
    path("categoria/eliminar/<int:id>/",
         eliminar_categoria, name="eliminar_categoria"),
]
