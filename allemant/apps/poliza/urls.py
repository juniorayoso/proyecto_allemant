from django.conf.urls import patterns, include, url
from apps.poliza import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
   
    
    url(r'^polizas/$', views.PolizasView.as_view(),name='lista_polizas'),
   	url(r'^nuevo/$', views.NuevoPolizaView.as_view(),name='nuevo_poliza'),
   	url(r'^(?P<id_poliza>\d+)/plan_pagos/$', views.PlanPagosView.as_view(),name='plan_pagos'),
   	url(r'^plan_pagos/$', views.PlanPagosView.as_view(),name='plan_pagos'),
   	url(r'^get_plan_pagos/$', views.GetPlanPagosView.as_view(),name='get_plan_pagos'),
    url(r'^editar/(?P<id_poliza>\d+)/$', views.EditarPolizaView.as_view(),name="editar_poliza"),
    url(r'^archivos/(?P<id_poliza>\d+)/$', views.ArchivoView.as_view(),name="agregar_archivo"),
    url(r'^plan_pagos/borrar_cupon/$', views.BorrarCuponView.as_view(),name='borrar_cupon'),
    url(r'^poliza/cobranza/$', views.CobranzaView.as_view(),name='cobranza'),

	
) 
