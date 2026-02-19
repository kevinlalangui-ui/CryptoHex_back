import secrets

from django.db import models


# definiendo roles en django
class Roles(models.Model):
    nombre = models.CharField(max_length=30, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True, verbose_name="¿Está activo?")

    class Meta:
        db_table = 'roles'
        ordering = ('nombre', 'is_active')
        verbose_name = '2. Role'
        verbose_name_plural = '2. Roles'

    # Este metodo es llamado al guardar y al actualizar
    def save(self, *args, **kwargs):
        if not self.slug:
            # Entonces creamos un slug unico
            prov = secrets.token_hex(16)
            # SELECT id FROM Roles WHERE slug=prov
            while Roles.objects.filter(slug=prov).exists():
                prov = secrets.token_hex(16)
            self.slug = prov

        super().save(*args, **kwargs)

    def __str__(self):
        return f"[ROL: {self.nombre}]"
