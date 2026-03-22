from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='inicio'),
    path("detalle-curso/<str:codigo>/", views.getByCodigo), #se llama en el fetch de gestionCursos.html
    path("registrarCurso/", views.registrarCurso),
    #-----------------------------------------------
    path("students/",views.getAllEstudents , name='students'),
    path("registrarStudent/", views.saveStudent),
    path("detail-student/<int:estudiante_id>/", views.getOneStudent),

    #hacer pdfs
    path("do-one-pdf/<int:id>/",views.generar_pdf),
]
