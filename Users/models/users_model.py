from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Usuario debe de tener un correo válido')
        if "@" not in email:
            raise ValueError('No es un formato de correo válido')

        if any(ext in email for ext in settings.EXTENSIONES_BLACKLIST):
            raise ValueError(
                f"No te voy a dejar crear una cuenta. Formatos no permitidos: " + ", ".join(
                    settings.EXTENSIONES_BLACKLIST))

        if not password:
            raise ValueError("Contraseña no válida")

        email = self.normalize_email(email)  # estandariza formato de ccorreo

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # eleva los permismos de un usuario, accesto total al panel de administración
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    is_active = models.BooleanField(default=True, verbose_name="¿Está activo?",
                                    help_text="(Obligatorio si queremos que el usuario pueda acceder a su cuenta)")

    role = models.ForeignKey('Roles', on_delete=models.SET_NULL, blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        ordering = ['-is_superuser', 'is_active', 'email']
        verbose_name = '1. Usuario'
        verbose_name_plural = '1. Usuarios'

    def __str__(self):
        return f"{self.nombre} ({self.email})"
