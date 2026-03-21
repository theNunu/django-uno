from django.shortcuts import render, redirect
from .models import Curso, Estudiante
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render, get_object_or_404
def home(request):
    cursos = Curso.objects.all()
    print("los cursos: ",cursos)
    return render(request, "gestionCursos.html", {"cursos": cursos})

def getAllEstudents(request):
    students = Estudiante.objects.all()
    print("los estudiantes: ",students)
    return render(request, "gestionStudents.html", {"students": students})


# def getByCodigo(request, codigo):
#     # Obtener el objeto por su clave primaria (pk) o ID
#     objeto = get_object_or_404(Curso, pk=codigo)
#     # print("detalle de un producto: ",objeto)
#     #    objeto = get_object_or_404(Cu0so, codigo=codigo) 
#     return render(request, 'cursoDetalle.html', {'item': objeto})

def getByCodigo(request, codigo):
    try:
        curso = Curso.objects.get(codigo=codigo)
        data = {
            'codigo': curso.codigo,
            'nombre': curso.nombre,
            'creditos': curso.creditos,
        }
        return JsonResponse(data)
    except Curso.DoesNotExist:
        return JsonResponse({'error': 'Curso no encontrado'}, status=404)

# def registrarCurso(request):
#     codigo = request.POST['txtCodigo']
#     nombre = request.POST['txtNombre']
#     creditos = request.POST['txtCredito']
#     curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
#     return redirect('/')

def registrarCurso(request):
    if request.method == 'POST':
        codigo = request.POST.get('txtCodigo')
        nombre = request.POST.get('txtNombre')
        creditos = request.POST.get('txtCredito')
        
        # Creamos el curso
        curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
        
        # Respondemos éxito
        return JsonResponse({
            'status': 'success',
            'message': 'Curso creado correctamente',
            'curso': {
                'codigo': curso.codigo,
                'nombre': curso.nombre,
                'creditos': curso.creditos
            }
        })
    return JsonResponse({'status': 'error'}, status=400)

def saveStudent(request):
    if request.method == 'POST':
        nombre = request.POST.get('txtNombre')
        apellido = request.POST.get('txtApellido')
        email = request.POST.get('txtEmail')
        curso_id = request.POST.get(252252)
        print('lleganos')
        
        # Creamos el curso
        student = Estudiante.objects.create(nombre=nombre, apellido=apellido, email=email, curso_id = curso_id)
        
        # Respondemos éxito
        return JsonResponse({
            'status': 'success',
            'message': 'Estudiante creado correctamente',
            'curso': {
                'nombre': student.nombre,
                'apellido': student.apellido,
                'email': student.email
            }
        })
    return JsonResponse({'status': 'error'}, status=400)
