
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path ('admin/', admin.site.urls),
    path ('', views.home, name='home'),
    path ('lista_pacotes/', views.visualiza_pacote, name='lista_pacotes'),
    path ('lista_detalhe_pacote/<id_pacote>', views.listar_detalhes_pacote, name='lista_detalhe_pacote'),
    path ('cadastro_pacote/', views.cadastro_pacote, name='cadastro_pacote')
]
