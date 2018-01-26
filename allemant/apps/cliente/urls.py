from django.conf.urls import patterns,url
from apps.cliente import views

urlpatterns = patterns('',

    
    url(r'^clientes/', views.ClientesView.as_view(),name='lista_clientes'),
  	url(r'^nuevo_cliente/(?P<tipo>\d+)/$', views.NuevoClienteView.as_view(),name='nuevo_cliente'),
  	url(r'^editar_cliente/(?P<id_cliente>\d+)/$', views.EditarClienteView.as_view(),name='editar_cliente'),

	# id_cliente  	
	url(r'^perfil_cliente/(?P<id_cliente>\d+)/$', views.PerfilClienteView.as_view(),name='perfil_cliente'),
	# editar_cliente
	url(r'^editar_perfil/(?P<id_cliente>\d+)/$', views.EditarPerfilView.as_view(),name='editar_perfil'),


)	