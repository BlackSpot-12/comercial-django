from django.shortcuts import render, redirect, get_object_or_404
from catalogo.models.categoria import Categoria
from catalogo.forms import CategoriaForm


def lista_categorias(request):
    lista_categorias = Categoria.objects.all()
    return render(request, "categoria/lista.html", context={'categorias': lista_categorias})


def agregar_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_categoria')
    else:
        form = CategoriaForm()

    return render(request, "categoria/agregar.html", context={'form': form})


def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('list_categoria')


def actualizar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('list_categoria')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, "categoria/agregar.html", context={'form': form})
