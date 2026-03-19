from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("/<str:codigo>/", views.getByCodigo, name="CursoDetalle"),
    path("registrarCurso/", views.registrarCurso),
]
