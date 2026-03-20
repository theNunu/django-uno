from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("detalle-curso/<str:codigo>/", views.getByCodigo), #se llama en el fetch de gestionCursos.html
    path("registrarCurso/", views.registrarCurso),
    #-----------------------------------------------
    path("students/",views.getAllEstudents)
]
