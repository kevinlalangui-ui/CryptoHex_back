import secrets

from django.db import models


# definiendo roles en django
class Roles(models.Model):
    nombre = models.CharField(max_length=30, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True, verbose_name="¿Está activo?")
    default = models.BooleanField(default=False, verbose_name="¿Rol por defecto?")

    class Meta:
        db_table = 'roles'
        ordering = ('nombre', 'is_active')
        verbose_name = '2. Role'
        verbose_name_plural = '2. Roles'

    # llamado al guradan y acutuiilizar
    def save(self, *args, **kwargs):
        if not self.slug: #si no tiene slug se le crea uno

            prov = secrets.token_hex(16)

            while Roles.objects.filter(slug=prov).exists():
                prov = secrets.token_hex(16)
            self.slug = prov
        rol_con_valor_por_defecto = Roles.objects.filter(default=True).first()

        if rol_con_valor_por_defecto and self.default and rol_con_valor_por_defecto.id != self.id:
            self.default = False

        super().save(*args, **kwargs)
        #se llma unicamente cunadod borramos
    def delete(self, *args, **kwargs):
        pass
    def __str__(self):
        return f"[ROL: {self.nombre}]"
