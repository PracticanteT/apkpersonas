"""
Configuración de URLs para el proyecto prointimopersonas.

La lista `urlpatterns` enruta URLs a vistas. Para más información, consulte:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Ejemplos:
Vistas basadas en funciones:
    1. Añada una importación:  from my_app import views
    2. Añada una URL a urlpatterns:  path('', views.home, name='home')
Vistas basadas en clases:
    1. Añada una importación:  from other_app.views import Home
    2. Añada una URL a urlpatterns:  path('', Home.as_view(), name='home')
Incluyendo otro URLconf:
    1. Importe la función include(): from django.urls import include, path
    2. Añada una URL a urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importa el módulo admin para la administración del sitio.
from django.contrib import admin
# Importa las funciones path y include para enrutar URLs.
from django.urls import path, include
# Importa las vistas paginaprincipal y user_login desde la aplicación empleados.
from empleados.views import paginaprincipal, user_login

# Definición de las rutas URL para el proyecto.
urlpatterns = [
    # Ruta para la administración del sitio.
    path('admin/', admin.site.urls),
    # Ruta para la vista de inicio de sesión del usuario.
    path('', user_login, name='user_login'),
    # Ruta para la vista de la página principal.
    path('', paginaprincipal, name='paginaprincipal'),
    # Incluye las URLs de la aplicación empleados.
    path('empleados/', include('empleados.urls')),
    # Incluye las URLs de la aplicación empleados (esto parece redundante y podría eliminarse).
    path('', include('empleados.urls')),
]
