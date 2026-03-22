from django.shortcuts import render, redirect
from .models import Curso, Estudiante
from django.http import JsonResponse

# Create your views here.
from django.shortcuts import render, get_object_or_404


def home(request):
    cursos = Curso.objects.all()
    print("los cursos: ", cursos)
    return render(request, "admin/courses/gestionCursos.html", {"cursos": cursos})


def getAllEstudents(request):
    students = Estudiante.objects.all()
    cursos = Curso.objects.all()
    print("los estudiantes: ", students)
    return render(
        request,
        "admin/students/GestionStudents.html",
        {"students": students, "cursos": cursos},
    )


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
            "codigo": curso.codigo,
            "nombre": curso.nombre,
            "creditos": curso.creditos,
        }
        return JsonResponse(data)
    except Curso.DoesNotExist:
        return JsonResponse({"error": "Curso no encontrado"}, status=404)


# def registrarCurso(request):
#     codigo = request.POST['txtCodigo']
#     nombre = request.POST['txtNombre']
#     creditos = request.POST['txtCredito']
#     curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
#     return redirect('/')


def registrarCurso(request):
    if request.method == "POST":
        codigo = request.POST.get("txtCodigo")
        nombre = request.POST.get("txtNombre")
        creditos = request.POST.get("txtCredito")

        # Creamos el curso
        curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)

        # Respondemos éxito
        return JsonResponse(
            {
                "status": "success",
                "message": "Curso creado correctamente",
                "curso": {
                    "codigo": curso.codigo,
                    "nombre": curso.nombre,
                    "creditos": curso.creditos,
                },
            }
        )
    return JsonResponse({"status": "error"}, status=400)


def saveStudent(request):
    if request.method == "POST":
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txtEmail")
        curso_id = request.POST.get("curso_id")
        # Creamos el curso
        student = Estudiante.objects.create(
            nombre=nombre, apellido=apellido, email=email, curso_id=curso_id
        )

        # Respondemos éxito
        return JsonResponse(
            {
                "status": "success",
                "message": "Estudiante creado correctamente",
                "curso": {
                    "nombre": student.nombre,
                    "apellido": student.apellido,
                    "email": student.email,
                    "curso_id": student.curso_id,
                },
            }
        )
    return JsonResponse({"status": "error"}, status=400)


def getOneStudent(request, estudiante_id):
    try:
        student = Estudiante.objects.get(estudiante_id=estudiante_id)
        course = Curso.objects.get(codigo=student.curso_id)

        print("contenido de curso", course, "nombre: ", course.nombre)
        # print("ESTUDIANTE SELECCIONADO", student.codigo.estudiante_id)
        data = {
            "estudiante_id": student.estudiante_id,
            "nombre": student.nombre,
            "apellido": student.apellido,
            "email": student.email,
            "id_curso": course.codigo,
            "course_name": course.nombre,
        }
        return JsonResponse(data)
    except Curso.DoesNotExist:
        return JsonResponse({"error": "Estudiante no encontrado"}, status=404)


###
# def saveStudent(request):
#     if request.method == 'POST':
#         nombre = request.POST.get('txtNombre')
#         apellido = request.POST.get('txtApellido')
#         email = request.POST.get('txtEmail')

#         # Capturamos el ID seleccionado en el select
#         id_seleccionado = request.POST.get('curso_id')

#         try:
#             # Creamos el estudiante vinculándolo al ID del curso
#             nuevo_estudiante = Estudiante.objects.create(
#                 nombre=nombre,
#                 apellido=apellido,
#                 email=email,
#                 curso_id=id_seleccionado # Django se encarga de la relación
#             )
#             return JsonResponse({'status': 'success', 'message': 'Estudiante registrado'})
#         except Exception as e:
#             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
###
