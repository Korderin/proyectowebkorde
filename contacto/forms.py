from django import forms


class FormularioContacto(forms.Form):
    nombre=forms.CharField(label='Nombre', max_length=100,required=True)
    email=forms.EmailField(label='email',required=True)
    contenido=forms.CharField(label='contenido',widget=forms.Textarea)
