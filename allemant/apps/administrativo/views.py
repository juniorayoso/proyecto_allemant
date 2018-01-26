from django.shortcuts import redirect
from django.shortcuts import get_list_or_404
from django.forms.models import modelformset_factory

from apps.administrativo import models, constants 
from apps.core import views as core_views
from apps.administrativo import forms 
from apps.core import forms as core_forms
from apps.core import models as core_models


class DocVentaView(core_views.AuthenticatedView):
    template_name = 'administrativo/documento_venta.html'
    lista_docventa = []
    
    def get(self, *args, **kwargs):
        self.lista_docventa = []
        ventas = []
        ventas = models.DocVenta.objects.filter()
        self.lista_docventa = []
        for docventa in ventas:
            docventa_detalle = {}
            docventa_detalle['id'] = docventa.id 
            
            if docventa.persona:
                docventa_detalle['numero_documento'] = docventa.numero_documento 
                docventa_detalle['nombre'] = docventa.persona
                
            else:
                docventa_detalle['numero_documento'] = docventa.numero_documento 
                docventa_detalle['nombre'] = docventa.empresa
                docventa_detalle['ruc'] = docventa.empresa.ruc
                
            
            docventa_detalle['fecha_emision'] = docventa.fecha_emision
            docventa_detalle['estado_doc_venta'] = docventa.estado_doc_venta
            docventa_detalle['igv'] = docventa.igv
            docventa_detalle['total'] = docventa.total

            self.lista_docventa.append(docventa_detalle)
        
        result = self.render_to_response(self.get_context_data())
        return result

    def get_context_data(self, **kwargs):
        context = super(DocVentaView, self).get_context_data(**kwargs)
        context['lista_docventa'] = self.lista_docventa
        
        return context

'''
class NuevoDocVentaView(core_views.AuthenticatedView):
    template_name = 'administrativo/nuevo_documento_venta.html'
'''
class NuevoDocVentaView(core_views.AuthenticatedView):
    template_name = 'administrativo/nuevo_documento_venta.html'
    ventas_form = None
    factura = False
    tipo_doc = None

    def get(self,request, tipo, *args, **kwargs):
        dic = {}
        if tipo=='0':
            dic = {'tipo_documento':constants.ID_TIPO_DOCUMENTO_FACTURA}
            
            self.factura = True
            self.tipo_doc = 0
        else:
            self.tipo_doc = 1
            dic = {'tipo_documento':constants.ID_TIPO_DOCUMENTO_BOLETA}

        self.ventas_form = forms.DocVentaForm(initial=dic)
        
        result = self.render_to_response(self.get_context_data())
        return result

    def post(self, request,tipo):
        self.ventas_form = forms.DocVentaForm(request.POST)
        
        if tipo=='0':
            
            self.factura = True
            self.tipo_doc = 0

            if self.ventas_form.is_valid():
                docventa=self.ventas_form.save()
                return redirect('nuevo_venta',0)
            else: 
                print self.ventas_form.errors    
            

        else:
            self.tipo_doc = 1  
            if self.ventas_form.is_valid():
                docventa=self.ventas_form.save()
                return redirect('nuevo_venta',1)
            else: 
                print self.ventas_form.errors  

        result = self.render_to_response(self.get_context_data())
        return result

    def get_context_data(self, **kwargs):
        context = super(NuevoDocVentaView, self).get_context_data(**kwargs)
        context['ventas_form'] = self.ventas_form
        context['factura'] = self.factura
        context['tipo_doc'] = self.tipo_doc
        
        return context












''''''
class DocCompraView(core_views.AuthenticatedView):
    template_name = 'administrativo/documento_compra.html'
    
class NuevoDocCompraView(core_views.AuthenticatedView):
    template_name = 'administrativo/nuevo_documento_compra.html'
