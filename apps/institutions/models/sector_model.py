from .commons.comon_catalog_model import CommonCatalog

class Sector(CommonCatalog):
    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectores"
    def __str__(self):
        return self.name