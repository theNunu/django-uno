from django.shortcuts import render, redirect
from .models import Curso
# Create your views here.
from django.shortcuts import render, get_object_or_404
def home(request):
    cursos = Curso.objects.all()
    print("los cursos: ",cursos)
    return render(request, "gestionCursos.html", {"cursos": cursos})


def getByCodigo(request, codigo):
    # Obtener el objeto por su clave primaria (pk) o ID
    objeto = get_object_or_404(Curso, pk=codigo)
    # print("detalle de un producto: ",objeto)
    #    objeto = get_object_or_404(Cu0so, codigo=codigo) 
    return render(request, 'cursoDetalle.html', {'item': objeto})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCredito']
    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')
