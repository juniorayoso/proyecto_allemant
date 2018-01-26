
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.shortcuts import redirect
from django.views.generic import TemplateView, View ,ListView

from apps.poliza import models 
from apps.core import models as core_models
from apps.poliza import forms 
from apps.core.views  import JSONResponseMixin,AuthenticatedView



from apps.poliza import utils_trama, utils_independiente




class PolizasView(AuthenticatedView):
    
    template_name = 'poliza/polizas.html'

    lista_polizas = []
    def get(self, *args, **kwargs):

        self.lista_polizas = models.Poliza.objects.filter()
        
        result = self.render_to_response(self.get_context_data())
        return result

    def get_context_data(self, **kwargs):
        context = super(PolizasView, self).get_context_data(**kwargs)
        context['lista_polizas'] = self.lista_polizas
       
        return context

class NuevoPolizaView(AuthenticatedView):
    template_name = 'poliza/nuevo_poliza.html'
    poliza_form = None
    riesgo_form = None
    # lista_polizas=None
    lista_polizas = []

    def get(self,request, *args, **kwargs):

        self.poliza_form = forms.PolizaForm()
        self.riesgo_form = modelformset_factory(models.Riesgo,form=forms.RiesgoForm,extra=1)
        self.riesgo_form = self.riesgo_form(queryset=models.Riesgo.objects.none())
        self.lista_polizas = models.Poliza.objects.filter()       
        result = self.render_to_response(self.get_context_data())
        return result

    def post(self, request):
        self.poliza_form = forms.PolizaForm(request.POST)  
        if self.poliza_form.is_valid():
            poliza=self.poliza_form.save()
            return redirect('editar_poliza',poliza.id)
        else:   
            print self.poliza_form.errors    
        
        result = self.render_to_response(self.get_context_data())
        return result


    def get_context_data(self, **kwargs):
        context = super(NuevoPolizaView, self).get_context_data(**kwargs)
        context['poliza_form'] = self.poliza_form
        context['riesgo_form'] = self.riesgo_form
        context['lista_polizas']= self.lista_polizas
        
        return context

class EditarPolizaView(TemplateView):

    template_name= "poliza/editar_poliza.html"
    poliza_form = None 
    poliza=None
    id_poliza=None
    lista_archivos=None
    archivo_form=None
    # ============== excel
    trama_form=None
    independiente_form=None
    file_trama = None
    file_independiente = None
    # ==============

    def get(self,request,id_poliza, *args, **kwargs):
        lista_polizas = models.Poliza.objects.filter(id=id_poliza)
        self.poliza = lista_polizas.first()
        self.poliza_form = forms.PolizaForm(instance=self.poliza)
        self.id_poliza=id_poliza
        
        # lista archivos
        self.lista_archivos = models.Archivo.objects.filter(poliza=self.poliza)
        print self.lista_archivos


        self.archivo_form=forms.ArchivoForm()

        #  == form para el excel ===
        self.trama_form = forms.TramaForm()
        self.independiente_form = forms.IndependienteForm()
        # ==========================

        result = self.render_to_response(self.get_context_data())
        return result


    def post(self,request,id_poliza):

        self.id_poliza = id_poliza

        self.poliza = models.Poliza.objects.filter(id=id_poliza)[0]
        self.poliza_form = forms.PolizaForm(request.POST,instance=self.poliza)
        if self.poliza_form.is_valid():
            self.poliza_form.save()


        self.trama_form = forms.TramaForm(request.POST, request.FILES)
        if self.trama_form.is_valid():
            self.file_trama = request.FILES['file_trama']

            result = utils_trama.handle_uploaded_file(self.file_trama, self.id_poliza)

            return redirect('lista_polizas')

        self.independiente_form = forms.IndependienteForm(request.POST , request.FILES)
        if self.independiente_form.is_valid():
            self.file_independiente = request.FILES['file_independiente']

            result = utils_independiente.handle_uploaded_file(self.file_independiente, self.id_poliza)

            return redirect('lista_polizas')


        return redirect("lista_polizas")


    def get_context_data(self, **kwargs):
        context = super(EditarPolizaView, self).get_context_data(**kwargs)
        context['poliza_form']= self.poliza_form
        context['id_poliza'] = self.id_poliza 
        context['lista_archivos'] = self.lista_archivos
        context['archivo_form'] = self.archivo_form 

        # ========= excel =======
        context['trama_form'] = self.trama_form
        context['independiente_form'] = self.independiente_form        
        # =======================

        return context



class PlanPagosView(AuthenticatedView):
    template_name = "poliza/plan_pagos.html"
    busqueda=False
    poliza = None
    plan_forms = None
    def get(self,request,id_poliza=None, *args, **kwargs):
        
        if id_poliza:
            planes=[]
            self.poliza = models.Poliza.objects.filter(id=id_poliza).first()
            planes = models.PlanPagos.objects.filter(poliza=self.poliza)
            dict_inicial =[]
            for x in xrange(1,int(self.poliza.cantidad_cuotas)+1):
                dict_inicial.append({'numero_cuota':x,'monto':round((self.poliza.prima/self.poliza.cantidad_cuotas),2)})

            if planes:
                plan_formset = modelformset_factory(models.PlanPagos,form=forms.PlanPagosForm,extra=0)
                self.plan_forms = plan_formset(queryset=planes)

            else:
                plan_formset = modelformset_factory(models.PlanPagos,form=forms.PlanPagosForm,extra=self.poliza.cantidad_cuotas)
                self.plan_forms = plan_formset(queryset=planes,initial=dict_inicial)
            
             
                

        else:
            self.busqueda = True

        result = self.render_to_response(self.get_context_data())
        return result

    def post(self,request,id_poliza=None):

        self.poliza = models.Poliza.objects.filter(id=id_poliza).first()
        plan_formset = modelformset_factory(models.PlanPagos,form=forms.PlanPagosForm,max_num=4,extra=self.poliza.cantidad_cuotas)
        planes = models.PlanPagos.objects.filter(poliza=self.poliza)
        if planes:
            formset = plan_formset(request.POST,queryset=planes)
        else:
            formset = plan_formset(request.POST)

        if formset.is_valid():
            planes = formset.save(commit=False)
            for plan in planes: 
                plan.poliza = self.poliza
                plan.save()

            
            return redirect('editar_poliza',self.poliza.id)

        else:
            print formset.errors

        result = self.render_to_response(self.get_context_data())
        return result


    def get_context_data(self, **kwargs):
        context = super(PlanPagosView, self).get_context_data(**kwargs)
        context['busqueda']= self.busqueda
        context['poliza']= self.poliza
        context['plan_forms']= self.plan_forms

        return context

class GetPlanPagosView(View,JSONResponseMixin):

    def get(self,request):

        data = {}
        poliza=None
        numero_poliza = request.GET.get('numero_poliza')
        lista_polizas = models.Poliza.objects.filter(numero_poliza=numero_poliza)
        if lista_polizas:
            poliza = models.Poliza.objects.filter(numero_poliza=numero_poliza).first()
        if poliza:

            data['id'] = poliza.id
            data['numero'] = poliza.numero_poliza
            data['cia'] = poliza.cia.razon_social
            data['cliente'] = str(poliza.cliente)
            data['monto'] = str(poliza.monto_asegurado)
            data['ramo'] = poliza.ramo.descripcion
            data['prima'] = str(poliza.prima)
            data['moneda'] = poliza.moneda.abreviatura
            data['cuotas'] = poliza.cantidad_cuotas
            data['fecha_inicio'] = str(poliza.fecha_inicio.date())
        
        result = data
        return self.render_to_response(result)


class ArchivoView(TemplateView):
    template_name="poliza/agregar_archivo.html"
    #template_name="poliza/editar_poliza.html"
    id_poliza=""
    archivo_form=None

    def get(self,request,id_poliza=None, *args, **kwargs):
        self.id_poliza=id_poliza
        self.archivo_form=forms.ArchivoForm()

        result = self.render_to_response(self.get_context_data())
        return result

    def post(self,request,id_poliza):
        poliza = models.Poliza.objects.filter(id=id_poliza)
        if poliza:
            
            self.archivo_form = forms.ArchivoForm(request.POST,\
                request.FILES)
            if self.archivo_form.is_valid():
                archivo = self.archivo_form.save(commit=False)
                archivo.poliza = poliza[0] 
                archivo.save()
            else:
                print self.archivo_form.errors 
            
            return redirect('editar_poliza',id_poliza)
        
        else: 
            
            result = self.render_to_response(self.get_context_data())
            return result


    def get_context_data(self, **kwargs):
        context = super(ArchivoView, self).get_context_data(**kwargs)
        context['id_poliza'] = self.id_poliza
        context['archivo_form'] = self.archivo_form
        return context

class BorrarCuponView(View,JSONResponseMixin):

    def get(self, request, *args, **kwargs):

        id_cupon = request.GET.get('id_cupon')
        cupones  = models.PlanPagos.objects.filter(id=id_cupon)
        if cupones:
            cupon= cupones.first()
            cupon.delete()

        return self.render_to_response(True)


class CobranzaView(TemplateView):
    template_name= "poliza/cobranza.html"
    cobranza_form = None
    cupones = []
    def get(self, request, *args, **kwargs):
        self.cobranza_form = forms.CobranzaForm()

        result = self.render_to_response(self.get_context_data())
        return result

    def post(self,request):
        self.cobranza_form = forms.CobranzaForm(request.POST)
        polizas = models.Poliza.objects.all()
        id_cia = self.cobranza_form.data['cia']
        if id_cia:
            polizas = polizas.filter(cia=id_cia)
        
        id_area = self.cobranza_form.data['area']
        if id_area:
            polizas = polizas.filter(cliente__area=id_area)

        self.cupones=[]
        for poliza in polizas:
            lista_cupones = models.PlanPagos.objects.filter(poliza=poliza)
            for cupon in lista_cupones:
                data_dict={}
                data_dict['numero_cuota'] = cupon.numero_cuota
                data_dict['numero_cupon'] = cupon.numero_cupon
                data_dict['cliente'] = poliza.cliente
                data_dict['telefono'] = core_models.Telefono.objects.filter(persona=poliza.cliente)[0]
                data_dict['poliza'] = poliza.numero_poliza
                data_dict['monto'] = cupon.monto
                data_dict['vencimiento'] = str(cupon.fecha_vence.date().strftime('%d/%m/%Y'))
                self.cupones.append(data_dict)


        
        result = self.render_to_response(self.get_context_data())
        return result

    def get_context_data(self,**kwargs):
        context = super(CobranzaView,self).get_context_data(**kwargs)
        context['cobranza_form'] = self.cobranza_form
        context['cupones'] = self.cupones
        return context

