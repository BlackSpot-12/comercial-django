from django import forms
from catalogo.models.categoria import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'border border-gray-400 rounded p-2 w-full mt-2 mb-4'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'border border-gray-400 rounded p-2 w-full mt-2 mb-4',
                'rows': 3
            }),
        }
