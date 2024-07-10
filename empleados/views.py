# Importa el modelo informacionempleado desde el módulo actual.
from .models import informacionempleado
# Importa los formularios InformacionEmpleadoForm y HijoFormSet desde el módulo actual.
from .forms import InformacionEmpleadoForm, HijoFormSet, EstudiosRealizadosFormSet
# Importa funciones de atajo desde django.shortcuts.
from django.shortcuts import render, redirect, get_object_or_404
# Importa funciones de autenticación desde django.contrib.auth.
from django.contrib.auth import authenticate, login as auth_login
# Importa el decorador login_required para requerir autenticación en las vistas.
from django.contrib.auth.decorators import login_required
# Importa mensajes desde django.contrib para mostrar mensajes al usuario.
from django.contrib import messages 
# Importa JsonResponse para devolver respuestas JSON.
from django.http import JsonResponse
# Importa el formulario de login personalizado.
from .forms import LoginForm
# Importa la función de logout desde django.contrib.auth.
from django.contrib.auth import logout
# Importa el decorador never_cache para evitar el almacenamiento en caché de las vistas.
from django.views.decorators.cache import never_cache
# Importa el decorador personalizado group_required para requerir que el usuario pertenezca a un grupo específico.
from prointimopersonas.decorators import group_required 
# Importa HttpResponseRedirect para redirigir con una respuesta HTTP.
from django.http import HttpResponseRedirect
# Importa reverse para obtener URLs por el nombre de la vista.
from django.urls import reverse

# Vista para el inicio de sesión de usuarios.
@never_cache
def user_login(request):
    # Si el usuario ya está autenticado, redirige a la página principal.
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('paginaprincipal'))

    # Si el método de la solicitud es POST, procesa el formulario de login.
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('paginaprincipal'))
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Vista para la página principal, requiere que el usuario esté autenticado.
@login_required
@never_cache
def paginaprincipal(request):
    return render(request, 'paginaprincipal.html')

# Vista para cerrar la sesión de un usuario.
def logout_view(request):
    logout(request)
    return redirect('/')

# Vista para ingresar un nuevo empleado, requiere autenticación y pertenecer al grupo 'admin'.
@login_required
@never_cache
@group_required('admin')
def ingresar_empleado(request):
    if request.method == 'POST':
        form_empleado = InformacionEmpleadoForm(request.POST)
        tiene_hijos = request.POST.get('tiene_hijos')
        formset_hijos = HijoFormSet(request.POST, request.FILES) if tiene_hijos == 'si' else HijoFormSet()
        formset_estudios = EstudiosRealizadosFormSet(request.POST, request.FILES)

        # Aquí verificamos si ambos formsets y el formulario principal son válidos
        if form_empleado.is_valid() and (tiene_hijos == 'no' or formset_hijos.is_valid()) and formset_estudios.is_valid():
            empleado = form_empleado.save()

            # Guarda los datos de los hijos si existen
            if tiene_hijos == 'si':
                hijos = formset_hijos.save(commit=False)
                for hijo in hijos:
                    hijo.informacion_empleado = empleado
                    hijo.save()
                formset_hijos.save_m2m()

            # Guarda los datos de los estudios realizados
            estudios = formset_estudios.save(commit=False)
            for estudio in estudios:
                estudio.informacionempleado = empleado
                estudio.save()
            formset_estudios.save_m2m()

            return JsonResponse({'success': True, 'message': 'Empleado creado correctamente.'})
        else:
            return JsonResponse({'success': False, 'message': 'Por favor corrija los errores en el formulario.'}, status=400)
    else:
        form_empleado = InformacionEmpleadoForm()
        formset_hijos = HijoFormSet()
        formset_estudios = EstudiosRealizadosFormSet()

    return render(request, 'ingresar_empleado.html', {
        'form_empleado': form_empleado,
        'formset_hijos': formset_hijos,
        'formset_estudios': formset_estudios
    })


# Vista para consultar un empleado, requiere autenticación y pertenecer al grupo 'lectores'.
@login_required
@never_cache
@group_required('lectores')
def consultar_empleado(request):
    empleado = None
    hijos = []
    estudios = []
    no_registro = False
    if request.method == 'POST':
        codigo_empleado = request.POST.get('codigo_empleado')
        cedula = request.POST.get('cedula')

        if codigo_empleado:
            try:
                empleado = informacionempleado.objects.get(codigo_empleado=codigo_empleado)
                hijos = empleado.hijos.all()
                estudios = empleado.estudios.all()
            except informacionempleado.DoesNotExist:
                no_registro = True
        elif cedula:
            try:
                empleado = informacionempleado.objects.get(cedula=cedula)
                hijos = empleado.hijos.all()
                estudios = empleado.estudios.all()
            except informacionempleado.DoesNotExist:
                no_registro = True

    return render(request, 'consultar_empleado.html', {
        'empleado': empleado,
        'hijos': hijos,
        'estudios': estudios,
        'no_registro': no_registro
    })


# Vista para actualizar un empleado, requiere autenticación y pertenecer al grupo 'admin'.
@login_required
@never_cache
@group_required('admin')
def actualizar_empleado(request, codigo_empleado):
    empleado = get_object_or_404(informacionempleado, codigo_empleado=codigo_empleado)
    if request.method == 'POST':
        form_empleado = InformacionEmpleadoForm(request.POST, instance=empleado)
        formset_hijos = HijoFormSet(request.POST, request.FILES, instance=empleado)
        formset_estudios = EstudiosRealizadosFormSet(request.POST, request.FILES, instance=empleado)

        if form_empleado.is_valid() and formset_hijos.is_valid() and formset_estudios.is_valid():
            form_empleado.save()
            hijos = formset_hijos.save(commit=False)
            for hijo in hijos:
                hijo.informacion_empleado = empleado
                hijo.save()
            formset_hijos.save_m2m()
            
            estudios = formset_estudios.save(commit=False)
            for estudio in estudios:
                estudio.informacion_empleado = empleado
                estudio.save()
            formset_estudios.save_m2m()

            return JsonResponse({'success': True, 'message': 'Empleado actualizado correctamente.'})
        else:
            return JsonResponse({'success': False, 'message': 'Por favor corrija los errores en el formulario.'}, status=400)
    else:
        form_empleado = InformacionEmpleadoForm(instance=empleado)
        formset_hijos = HijoFormSet(instance=empleado)
        formset_estudios = EstudiosRealizadosFormSet(instance=empleado)
    
    return render(request, 'actualizar_empleado.html', {
        'form_empleado': form_empleado,
        'formset_hijos': formset_hijos,
        'formset_estudios': formset_estudios,
        'empleado': empleado
    })
# Vista para buscar un empleado para actualizar, requiere autenticación y pertenecer al grupo 'admin'.
@login_required
@never_cache
@group_required('admin')  # Solo para administradores
def buscar_empleado_para_actualizar(request):
    no_registro = False  # Nueva bandera para controlar el mensaje de error
    if request.method == 'POST':
        codigo_empleado = request.POST.get('codigo_empleado')
        try:
            empleado = informacionempleado.objects.get(codigo_empleado=codigo_empleado)
            return redirect('actualizar_empleado', codigo_empleado=codigo_empleado)
        except informacionempleado.DoesNotExist:
            no_registro = True

    return render(request, 'buscar_empleado_para_actualizar.html', {'no_registro': no_registro})
