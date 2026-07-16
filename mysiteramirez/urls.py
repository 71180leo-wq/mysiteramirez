"""
URL configuration for mysiteramirez project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
URL configuration for mysiteramirez project.
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    
    # Módulos Base
    path("pageclientes/", include("clientes.urls")),
    path("pageproveedores/", include("proveedores.urls")),
    path("pageempleados/", include("empleados.urls")),
    path("pageproductos/", include("productos.urls")),
    path("pageusuarios/", include("usuarios.urls")),
    
    # Módulos Transaccionales
    path("pageventas/", include("ventas.urls")),
    path("pagecompras/", include("compras.urls")),
    
    # Módulos de Organización
    path("pagegrupos/", include("grupos.urls")),
    path("pagesucursal/", include("sucursal.urls")),
    path("pageinventario/", include("inventario.urls")),

    
    # 🌟 COMENTADO TEMPORALMENTE PARA EVITAR EL ATTRIBUTERROR
    # Cuando termines tu archivo inventario/views.py le quitas el '#' de abajo:
    # path("pageinventario/", include("inventario.urls")),
]




# path es el que manda llamara a las  urls que contienen las llmadas a la vista
