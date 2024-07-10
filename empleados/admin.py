#Registro de modelos
from django.contrib import admin
from .models import informacionempleado  # Asegúrate de que la importación del modelo sea correcta

class InformacionEmpleadoAdmin(admin.ModelAdmin):
    list_display = ['codigo_empleado', 'nombre', 'apellido', 'fecha_de_nacimiento', 'estado']  # Ajusta los campos que quieras mostrar
    search_fields = ['codigo_empleado', 'nombre', 'apellido']  # Campos por los cuales se puede buscar

# Registra el modelo usando la clase de admin personalizada
admin.site.register(informacionempleado, InformacionEmpleadoAdmin)
