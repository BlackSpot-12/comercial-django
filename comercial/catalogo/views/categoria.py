from django.shortcuts import render


def lista_categorias(request):

    lista_categorias = [
        {'id': 1, 'nombre': 'tv', 'descripcion': 'Televisores de alta gama'},
        {'id': 2, 'nombre': 'Laptop', 'descripcion': 'Computadoras portátiles'}
    ]
    return render(request, "categoria/lista.html", context={'categorias': lista_categorias})
