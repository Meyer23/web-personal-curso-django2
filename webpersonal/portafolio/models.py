from django.db import models

# Create your models here.
class Project(models.Model): 
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to="projects")
    link = models.URLField(verbose_name = "Dirección Web", null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')


    class Meta: 
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ["-create"]

    def __str__(self):
        return self.title
    