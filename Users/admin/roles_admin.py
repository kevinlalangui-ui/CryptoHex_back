from django.contrib import admin

from Users.models import Roles


class RolesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    readonly_fields = ('slug',)

    fieldsets = (
        ("Información", {'fields': ('nombre',),}),
        ("Configuración", {'fields': ('is_active', 'slug'),}),
    )


admin.site.register(Roles, RolesAdmin)
