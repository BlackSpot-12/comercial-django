from django.contrib import admin
from django.urls import path
from catalogo.views.categoria import lista_categorias, agregar_categoria, eliminar_categoria, actualizar_categoria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categoria/', lista_categorias, name='list_categoria'),
    path('categoria/agregar/', agregar_categoria, name='agregar_categoria'),
    path('categoria/eliminar/<int:id>/',
         eliminar_categoria, name='eliminar_categoria'),
    path('categoria/actualizar/<int:id>/',
         actualizar_categoria, name='actualizar_categoria'),
]
