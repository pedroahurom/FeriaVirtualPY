from .commons.comon_catalog_model import CommonCatalog

class InstitutionType(CommonCatalog):
    class Meta:
        verbose_name = "Tipo de institucion"
        verbose_name_plural = "Tipos de instituciones"

    def __str__(self):
        return self.name