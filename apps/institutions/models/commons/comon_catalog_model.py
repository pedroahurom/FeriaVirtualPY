from django.db import models

# Modelo base con atributos comunes
class CommonCatalog(models.Model):
    name = models.CharField(max_length=150)
    class Meta:
        abstract = True