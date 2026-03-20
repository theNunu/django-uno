from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.codigo, self.nombre, self.creditos)

class Estudiante(models.Model):
    # Definimos el ID personalizado
    estudiante_id = models.AutoField(primary_key=True)
    # Relación de Uno a Muchos
    #related_name='estudiantes': Esto es muy útil. Te permite acceder a los estudiantes desde un objeto curso fácilmente (ejemplo: mi_curso.estudiantes.all()).
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='estudiantes')
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    