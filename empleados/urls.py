# Importa la función path desde django.urls para definir las rutas.
from django.urls import path
# Importa las vistas desde el módulo actual.
from .views import paginaprincipal, consultar_empleado, ingresar_empleado, actualizar_empleado, buscar_empleado_para_actualizar, user_login, logout_view
# Importa vistas de autenticación desde django.contrib.auth.
from django.contrib.auth import views as auth_views

# Define la lista de rutas (URLs) para la aplicación.
urlpatterns = [
    
    # Define una ruta para la página principal.
    path('paginaprincipal/', paginaprincipal, name='paginaprincipal'),
    
    # Define una ruta para consultar empleados.
    path('consultar-empleado/', consultar_empleado, name='consultar_empleado'),
    
    # Define una ruta para ingresar un nuevo empleado.
    path('ingresar-empleado/', ingresar_empleado, name='ingresar_empleado'),
    
    # Define una ruta para actualizar un empleado específico usando el código del empleado en la URL.
    path('actualizar-empleado/<str:codigo_empleado>/', actualizar_empleado, name='actualizar_empleado'),
    
    # Define una ruta para buscar un empleado que se va a actualizar.
    path('buscar-empleado-para-actualizar/', buscar_empleado_para_actualizar, name='buscar_empleado_para_actualizar'),
    
    # Define una ruta para la página de inicio de sesión.
    path('login/', user_login, name='login'),
    
    # Define una ruta para la función de cierre de sesión.
    path('logout/', logout_view, name='logout'),
]
