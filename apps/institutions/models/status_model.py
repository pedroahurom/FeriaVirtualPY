from .commons.comon_catalog_model import CommonCatalog


class Status(CommonCatalog):
    class Meta:
        verbose_name = "Estatus"
        verbose_name_plural = "Estatus"

    def __str__(self):
        return self.name