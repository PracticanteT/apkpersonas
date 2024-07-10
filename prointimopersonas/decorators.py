# Importa decorator_from_middleware_with_args para crear decoradores a partir de middleware.
from django.utils.decorators import decorator_from_middleware_with_args
# Importa CacheMiddleware para el control de caché en las vistas.
from django.middleware.cache import CacheMiddleware
# Importa user_passes_test para crear decoradores basados en pruebas de usuario.
from django.contrib.auth.decorators import user_passes_test
# Importa redirect para redirigir usuarios a diferentes vistas.
from django.shortcuts import redirect
# Importa messages para mostrar mensajes a los usuarios.
from django.contrib import messages

# Definimos el decorador no_cache usando CacheMiddleware para evitar el almacenamiento en caché de las vistas.
no_cache = decorator_from_middleware_with_args(CacheMiddleware)(
    cache_control={
        'no_cache': True,           # No almacenar en caché.
        'no_store': True,           # No almacenar en ninguna tienda.
        'must_revalidate': True,    # Revalidar la caché con el servidor.
        'max_age': 0,               # La caché debe expirar inmediatamente.
        'private': True,            # Indica que la caché es privada para el usuario.
    }
)

# Definimos un decorador que verifica si el usuario pertenece a un grupo específico.
def group_required(group_name):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            # Verifica si el usuario pertenece al grupo especificado o si es superusuario.
            if request.user.groups.filter(name=group_name).exists() or request.user.is_superuser:
                # Si cumple la condición, ejecuta la vista.
                return view_func(request, *args, **kwargs)
            else:
                # Si no cumple la condición, muestra un mensaje de error y redirige a la página principal.
                messages.error(request, 'No tiene permiso para acceder a esta página.')
                return redirect('paginaprincipal')
        return _wrapped_view
    return decorator
