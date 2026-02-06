from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Users.models import CustomUser


class InfoPersonalInline(admin.StackedInline):
    can_delete = False
    verbose_name = "Información personal"
    verbose_name_plural = "Datos personales"


class CustomUserAdmin(UserAdmin):
    # inlines = (InfoPersonalInline,)
    # model = CustomUser

    # Esto las columnas en la tabla de mi panel de admin.
    list_display = ('email', 'nombre', 'apellidos', 'is_active', 'role__nombre', 'last_login')

    # Añade una barra de filtro. Le decimos que valores usaremos para filtrar.
    list_filter = ('is_active', 'is_superuser')

    # Añade una barra de búsqueda. Le decimos que valores usaremos para buscar.
    search_fields = ('email', 'nombre')

    # Añade un campo editable. Le decimos que valores queremos editar.
    list_editable = ('is_active',)

    list_per_page = 25

    ordering = ('-email',)

    fieldsets = (
        ("Inicio de sesión", {'fields': ('email', 'password')}),
        ("Información personal", {'fields': ('nombre', 'apellidos')}),
        ("Configuración", {'fields': ('is_active', 'is_staff', 'is_superuser', 'role')}),
    )

    add_fieldsets = (
        ("Información personal", {
            'classes': ('wide',),
            'fields': ('nombre', 'apellidos')}
         ),
        ("Información de iniciar sesión", {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
        ("Configuración", {
            'classes': ('wide',),
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser',)}
         ),
    )
# mirar si en la bd hemos configurado en el archivo info_ppersonal el nombre (user)
# tendremos que cambiar esa info a inicio de sesion junto con passwrod

admin.site.register(CustomUser, CustomUserAdmin)