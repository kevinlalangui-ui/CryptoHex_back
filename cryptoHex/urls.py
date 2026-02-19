from django.contrib import admin
from django.urls import path,include
#personalizacion de sitio de admin
admin.site.site_header = "Crypto Hex Administración"
admin.site.site_title = "Administración"
admin.site.index_title = "Administración versión: 1.0.0"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Users.urls')),
]
