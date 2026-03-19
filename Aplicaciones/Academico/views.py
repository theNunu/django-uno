from django.shortcuts import render
from .models import Curso
# Create your views here.

def home(request):
    cursos = Curso.objects.all()
    print("los cursos: ",cursos)
    return render(request, "gestionCursos.html", {"cursos": cursos})
