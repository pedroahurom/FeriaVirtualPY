from django.db import models
from apps.user.models.user_model import User

# Create your models here.

class Institution(models.Model):
    name = models.CharField(max_length=125, unique=True)
    clave_centro_trabajo = models.CharField(max_length=100)
    logo_recurso = models.ImageField(upload_to='logos/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Institucion"
        verbose_name_plural = "Instituciones"
        #db_table = 'institution'
    def __str__(self):
        return self.name
