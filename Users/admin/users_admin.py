from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Users.models import CustomUser

class CustomUserAdmin(UserAdmin):
    # inlines = (InfoPersonalInline,)
    # model = CustomUser

    # Esto las columnas en la tabla de mi panel de admin.
    list_display = ('email', 'nombre', 'is_active', 'role__nombre', 'last_login')

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
        ("Información personal", {'fields': ('nombre')}),
        ("Configuración", {'fields': ('is_active', 'is_staff', 'is_superuser', 'role')}),
    )

    add_fieldsets = (
        ("Información personal", {
            'classes': ('wide',),
            'fields': ('nombre', '')}#mirarr
         ),
        ("Información de iniciar sesión", {
            'classes': ('wide',),
            'fields': ('email1', 'email2', 'password')}
         ),
        ("Configuración", {
            'classes': ('wide',),
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser',)}
         ),
    )


admin.site.register(CustomUser, CustomUserAdmin)