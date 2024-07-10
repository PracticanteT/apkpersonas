# Importa la clase AppConfig del módulo django.apps.
from django.apps import AppConfig

# Define una nueva clase llamada EmpleadosConfig que hereda de AppConfig.
class EmpleadosConfig(AppConfig):
    # Define el tipo de campo automático predeterminado para los modelos en esta aplicación.
    default_auto_field = 'django.db.models.BigAutoField'
    # Especifica el nombre de la aplicación Django.
    name = 'empleados'
