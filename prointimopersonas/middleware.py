# Importa redirect para redirigir usuarios a diferentes vistas.
from django.shortcuts import redirect
# Importa MiddlewareMixin para compatibilidad con middlewares personalizados.
from django.utils.deprecation import MiddlewareMixin

# Definimos un middleware personalizado para la autenticación.
class AuthenticationMiddleware:
    # Inicializa el middleware con la función de respuesta.
    def __init__(self, get_response):
        self.get_response = get_response

    # Llama al middleware en cada solicitud.
    def __call__(self, request):
        # Verifica si el usuario no está autenticado y la ruta no es '/login'.
        if not request.user.is_authenticated and not request.path.startswith('/login'):
            # Redirige al usuario a la página de login si no está autenticado.
            return redirect('login')
        # Llama a la función de respuesta y devuelve la respuesta.
        response = self.get_response(request)
        return response

# Definimos un middleware personalizado para desactivar la caché.
class DisableCacheMiddleware(MiddlewareMixin):
    # Procesa la respuesta antes de devolverla al cliente.
    def process_response(self, request, response):
        # Añade encabezados a la respuesta para desactivar la caché.
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        # Devuelve la respuesta modificada.
        return response
