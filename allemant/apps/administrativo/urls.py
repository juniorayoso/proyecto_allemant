from django.conf.urls import patterns, url
from apps.administrativo import views
from django.contrib import admin
admin.autodiscover()

   
urlpatterns = patterns('',
  
  url(r'^documento_venta/$', views.DocVentaView.as_view(),name='ventas'),
  #url(r'^nuevo_documento_venta/$', views.NuevoDocVentaView.as_view(),name='nuevo_venta'),
  url(r'^nuevo_documento_venta/(?P<tipo>\d+)/$', views.NuevoDocVentaView.as_view(),name='nuevo_venta'),
  url(r'^documento_compra/$', views.DocCompraView.as_view(),name='compras'),
  url(r'^nuevo_documento_compra/$', views.NuevoDocCompraView.as_view(),name='nuevo_compra'),
)