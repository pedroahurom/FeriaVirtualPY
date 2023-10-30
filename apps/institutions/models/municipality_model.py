from .commons.comon_catalog_model import CommonCatalog
from django.db import models


class Municipality(CommonCatalog):

    source_shield = models.ImageField(upload_to='shield/', null=True, blank=True)
    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"

    def __str__(self):
        return self.name