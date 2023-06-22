from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index" ),
    path('nosotros',views.nosotros, name="nosotros"),
    path("catalogo",views.catalogo, name="catalogo"),
    path('iniciar_sesion', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('registro',views.registro,name="registro"),
    path('cambio_password',views.cambio_password,name="cambio_password"),
    path('perfil',views.perfil,name="perfil"),
    path('recuperar_password',views.recuperar_password,name="recuperar_password"),

    path('arte', views.arte, name="arte"),
    path('arte_add', views.arte_add, name="arte_add"),
    path('arte_edit/<str:idArticulo>', views.arte_edit, name="arte_edit"),
]