from django import forms
from .models import informacionempleado, Hijo, estudiosRealizados
from django.forms import inlineformset_factory
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'value': ''})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'value': ''})
    )

class InformacionEmpleadoForm(forms.ModelForm):
    class Meta:
        model = informacionempleado
        fields = '__all__'
        widgets = {
            'fecha_de_nacimiento': forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date'}),
            'fecha_de_ingreso': forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date'}),
            'fecha_de_retiro': forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(InformacionEmpleadoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.DateInput):
                field.widget.attrs['value'] = self.initial.get(field_name, '') 

    def clean(self):
        cleaned_data = super().clean()
        estado = cleaned_data.get('estado')
        fecha_de_retiro = cleaned_data.get('fecha_de_retiro')
        motivo_de_retiro = cleaned_data.get('motivo_de_retiro')

        if estado == 'Activo' and (fecha_de_retiro or motivo_de_retiro):
            raise forms.ValidationError(
                "Debido a que el usuario está activo, no se puede insertar información en 'Fecha de Retiro' o 'Motivo de Retiro'."
            )
        
        return cleaned_data


class HijoForm(forms.ModelForm):
    class Meta:
        model = Hijo
        fields = ['genero', 'nombre', 'apellido', 'fecha_de_nacimiento']
        widgets = {
            'fecha_de_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

HijoFormSet = inlineformset_factory(informacionempleado, Hijo, form=HijoForm, extra=1, can_delete=True)

class EstudiosRealizadosForm(forms.ModelForm):
    class Meta:
        model = estudiosRealizados
        fields = ['Nivel', 'Area', 'Institucion']
        widgets = {
            'Nivel': forms.Select(attrs={'class': 'form-control'}),
            'Area': forms.Select(attrs={'class': 'form-control'}),
            'Institucion': forms.TextInput(attrs={'class': 'form-control'})
        }

EstudiosRealizadosFormSet = inlineformset_factory(informacionempleado, estudiosRealizados, form=EstudiosRealizadosForm, fk_name='informacionempleado', extra=1, can_delete=True)
