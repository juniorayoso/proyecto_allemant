from django.shortcuts import redirect
from django.shortcuts import get_list_or_404 , get_object_or_404
from django.forms.models import modelformset_factory

from apps.cliente import models
from apps.core import views as core_views
from apps.cliente import forms
from apps.core import forms as core_forms
from apps.core import models as core_models
from apps.cliente import constants


from django.http import Http404


# Create your views here.

class ClientesView(core_views.AuthenticatedView):
    template_name = 'cliente/clientes.html'
    lista_clientes = []

    def get(self, *args, **kwargs):
        self.lista_clientes = []
        clientes = []
        clientes = models.Cliente.objects.filter()
        self.lista_clientes = []
        for cliente in clientes:
            cliente_detalle = {}
            cliente_detalle['id'] = cliente.id

            if cliente.persona:
                cliente_detalle['doi'] = cliente.persona.dni
                cliente_detalle['nombre'] = cliente.persona
                cliente_detalle['direccion'] = core_models.Direccion.objects.filter(
                    persona=cliente.persona).first()
                cliente_detalle['telefono'] = core_models.Telefono.objects.filter(
                    persona=cliente.persona).first()
                cliente_detalle['email'] = core_models.Email.objects.filter(
                    persona=cliente.persona).first()
            else:
                cliente_detalle['doi'] = cliente.empresa.ruc
                cliente_detalle['nombre'] = cliente.empresa
                cliente_detalle['direccion'] = core_models.Direccion.objects.filter(
                    empresa=cliente.empresa).first()
                cliente_detalle['telefono'] = core_models.Telefono.objects.filter(
                    empresa=cliente.empresa).first()
                cliente_detalle['email'] = core_models.Email.objects.filter(
                    empresa=cliente.persona).first()

            cliente_detalle['ejecutivo'] = cliente.ejecutivo
            cliente_detalle['vendedor'] = cliente.vendedor
            cliente_detalle['grupo'] = cliente.grupo_economico

            self.lista_clientes.append(cliente_detalle)

        result = self.render_to_response(self.get_context_data())
        return result

    def get_context_data(self, **kwargs):
        context = super(ClientesView, self).get_context_data(**kwargs)
        context['lista_clientes'] = self.lista_clientes

        return context


class NuevoClienteView(core_views.AuthenticatedView):
    template_name = 'cliente/nuevo_cliente.html'
    cliente_form = None
    persona_form = None
    cliente_natural = False
    telefono_form = None
    direccion_form = None
    email_form = None
    empresa_form = None
    tipo_cliente = None

    def get(self, request, tipo=None, *args, **kwargs):

        self.cliente_form = forms.ClienteForm()
        self.direccion_form = modelformset_factory(
            core_models.Direccion, form=core_forms.DireccionForm, extra=1)
        self.direccion_form = self.direccion_form(
            prefix="direccion", queryset=core_models.Direccion.objects.none())
        self.email_form = modelformset_factory(
            core_models.Email, form=core_forms.EmailForm, extra=1)
        self.email_form = self.email_form(
            prefix="email", queryset=core_models.Telefono.objects.none())
        self.telefono_form = modelformset_factory(
            core_models.Telefono, form=core_forms.TelefonoForm, extra=1)
        self.telefono_form = self.telefono_form(
            prefix="telefono", queryset=core_models.Telefono.objects.none())
        if tipo == '0':
            self.persona_form = core_forms.PersonaForm()
            self.cliente_natural = True
            self.tipo_cliente = 0
        else:
            self.tipo_cliente = 1
            self.empresa_form = core_forms.EmpresaForm()

        #import pdb
        # pdb.set_trace()
        result = self.render_to_response(self.get_context_data())
        return result

    def post(self, request, tipo=None):
        self.cliente_form = forms.ClienteForm(request.POST)
        self.email_form = modelformset_factory(
            core_models.Email, form=core_forms.EmailForm, extra=1)
        self.email_form = self.email_form(
            request.POST, queryset=core_models.Email.objects.none(), prefix="email")
        self.direccion_form = modelformset_factory(
            core_models.Direccion, form=core_forms.DireccionForm, extra=1)
        self.direccion_form = self.direccion_form(
            request.POST, queryset=core_models.Direccion.objects.none(), prefix="direccion")
        self.telefono_form = modelformset_factory(
            core_models.Telefono, form=core_forms.TelefonoForm, extra=1)
        self.telefono_form = self.telefono_form(
            request.POST, queryset=core_models.Telefono.objects.none(), prefix="telefono")

        if tipo == '0':
            self.tipo_cliente = 0
            self.cliente_natural = True
            self.persona_form = core_forms.PersonaForm(request.POST)

            if self.persona_form.is_valid():

                persona = self.persona_form.save(commit=False)
                telefono = self.telefono_form.save(commit=False)

                for fono in telefono:
                    fono.persona = persona
                    fono.save()

                ubicaciones = self.direccion_form.save(commit=False)
                for ubicacion in ubicaciones:
                    ubicacion.persona = persona
                    ubicacion.save()

                email = self.email_form.save(commit=False)

                for mail in email:
                    mail.persona = persona
                    mail.save()

                if self.cliente_form.is_valid():
                    persona.save()
                    cliente = self.cliente_form.save(commit=False)
                    cliente.persona = persona
                    self.cliente_form.save()
                    return redirect('lista_clientes')
            else:
                print self.persona_form.errors

        else:
            self.tipo_cliente = 1
            self.empresa_form = core_forms.EmpresaForm(request.POST)

            if self.empresa_form.is_valid():

                empresa = self.empresa_form.save()

                telefono = self.telefono_form.save(commit=False)
                for fono in telefono:
                    fono.empresa = empresa
                    fono.save()

                ubicaciones = self.direccion_form.save(commit=False)
                for ubicacion in ubicaciones:
                    ubicacion.empresa = empresa
                    ubicacion.save()

                email = self.email_form.save(commit=False)
                for mail in email:
                    mail.empresa = empresa
                    mail.save()

                if self.cliente_form.is_valid():
                    cliente = self.cliente_form.save(commit=False)
                    cliente.empresa = empresa
                    self.cliente_form.save()
                    return redirect('lista_clientes')

        result = self.render_to_response(self.get_context_data())
        return result

    def get_context_data(self, **kwargs):
        context = super(NuevoClienteView, self).get_context_data(**kwargs)
        context['cliente_form'] = self.cliente_form
        context['persona_form'] = self.persona_form
        context['cliente_natural'] = self.cliente_natural
        context['telefono_form'] = self.telefono_form
        context['direccion_form'] = self.direccion_form
        context['email_form'] = self.email_form
        context['empresa_form'] = self.empresa_form
        context['tipo_cliente'] = self.tipo_cliente

        return context


class EditarClienteView(core_views.AuthenticatedView):
    template_name = 'cliente/editar_cliente.html'
    cliente_form = None
    persona_form = None
    cliente_natural = False
    telefono_form = None
    direccion_form = None
    email_form = None
    empresa_form = None
    tipo_cliente = None
    id_cliente = None

    def get(self, request, id_cliente=None, *args, **kwargs):
        cliente = get_list_or_404(models.Cliente, pk=id_cliente)[0]

        self.id_cliente = id_cliente
        self.cliente_form = forms.ClienteForm(instance=cliente)
        if cliente.persona:

            direccion = core_models.Direccion.objects.filter(
                persona=cliente.persona)
            telefono = core_models.Telefono.objects.filter(
                persona=cliente.persona)
            email = core_models.Email.objects.filter(persona=cliente.persona)
            self.persona_form = core_forms.PersonaForm(
                instance=cliente.persona)

            self.cliente_natural = True
            self.tipo_cliente = 0
        else:
            direccion = core_models.Direccion.objects.filter(
                empresa=cliente.empresa)
            telefono = core_models.Telefono.objects.filter(
                empresa=cliente.empresa)
            email = core_models.Email.objects.filter(empresa=cliente.empresa)
            self.tipo_cliente = 1
            self.empresa_form = core_forms.EmpresaForm(
                instance=cliente.empresa)

        self.direccion_form = modelformset_factory(
            core_models.Direccion, form=core_forms.DireccionForm, extra=0)
        self.direccion_form = self.direccion_form(
            prefix="direccion", queryset=direccion)
        self.telefono_form = modelformset_factory(
            core_models.Telefono, form=core_forms.TelefonoForm, extra=0)
        self.telefono_form = self.telefono_form(
            prefix="telefono", queryset=telefono)
        self.email_form = modelformset_factory(
            core_models.Email, form=core_forms.EmailForm, extra=0)
        self.email_form = self.email_form(prefix="email", queryset=email)
        result = self.render_to_response(self.get_context_data())
        return result

    def post(self, request, id_cliente=None):
        cliente = get_list_or_404(models.Cliente, pk=id_cliente)[0]

        self.cliente_form = forms.ClienteForm(request.POST, instance=cliente)

        if cliente.persona:
            self.persona_form = core_forms.PersonaForm(
                request.POST, instance=cliente.persona)
            direccion = core_models.Direccion.objects.filter(
                persona=cliente.persona)
            telefono = core_models.Telefono.objects.filter(
                persona=cliente.persona)
            email = core_models.Email.objects.filter(persona=cliente.persona)
            if self.persona_form.is_valid():
                persona = self.persona_form.save()
                self.telefono_form = modelformset_factory(
                    core_models.Telefono, form=core_forms.TelefonoForm, extra=1)
                self.telefono_form = self.telefono_form(
                    request.POST, queryset=telefono, prefix="telefono")

                telefono = self.telefono_form.save(commit=False)
                for fono in telefono:
                    fono.persona = persona
                    fono.save()

                self.direccion_form = modelformset_factory(
                    core_models.Direccion, form=core_forms.DireccionForm, extra=1)
                self.direccion_form = self.direccion_form(
                    request.POST, prefix="direccion", queryset=direccion)

                ubicaciones = self.direccion_form.save(commit=False)
                for ubicacion in ubicaciones:
                    ubicacion.persona = persona
                    ubicacion.save()

                self.email_form = modelformset_factory(
                    core_models.Email, form=core_forms.EmailForm, extra=1)

                self.email_form = self.email_form(
                    request.POST, queryset=email, prefix="email")
                email = self.email_form.save(commit=False)
                for mail in email:
                    mail.persona = persona
                    mail.save()

                if self.cliente_form.is_valid():
                    cliente_instance = self.cliente_form.save(commit=False)
                    cliente_instance.persona = persona
                    self.cliente_form.save()
                else:
                    print self.cliente_form.errors

            else:
                print self.persona_form.errors

        else:
            self.empresa_form = core_forms.EmpresaForm(
                request.POST, instance=cliente.empresa)
            direccion = core_models.Direccion.objects.filter(
                empresa=cliente.empresa)
            telefono = core_models.Telefono.objects.filter(
                empresa=cliente.empresa)
            email = core_models.Email.objects.filter(empresa=cliente.empresa)

            if self.empresa_form.is_valid():

                empresa = self.empresa_form.save()
                self.telefono_form = modelformset_factory(
                    core_models.Telefono, form=core_forms.TelefonoForm, extra=1)
                self.telefono_form = self.telefono_form(
                    request.POST, queryset=telefono, prefix="telefono")

                for fono in telefono:
                    fono.empresa = empresa
                    fono.save()

                self.direccion_form = modelformset_factory(
                    core_models.Direccion, form=core_forms.DireccionForm, extra=1)
                self.direccion_form = self.direccion_form(
                    request.POST, prefix="direccion", queryset=direccion)

                ubicaciones = self.direccion_form.save(commit=False)
                for ubicacion in ubicaciones:
                    ubicacion.empresa = empresa
                    ubicacion.save()

                self.email_form = modelformset_factory(
                    core_models.Email, form=core_forms.EmailForm, extra=1)
                self.email_form = self.email_form(
                    request.POST, queryset=email, prefix="email")

                for mail in email:
                    mail.persona = persona
                    mail.save()

                if self.cliente_form.is_valid():

                    cliente_instance = self.cliente_form.save(commit=False)
                    cliente_instance.empresa = empresa
                    self.cliente_form.save()
                else:
                    print self.cliente_form.errors

            else:
                print self.empresa_form.errors

        return redirect('lista_clientes')

    def get_context_data(self, **kwargs):
        context = super(EditarClienteView, self).get_context_data(**kwargs)
        context['cliente_form'] = self.cliente_form
        context['persona_form'] = self.persona_form
        context['cliente_natural'] = self.cliente_natural
        context['telefono_form'] = self.telefono_form
        context['direccion_form'] = self.direccion_form
        context['email_form'] = self.email_form
        context['empresa_form'] = self.empresa_form
        context['tipo_cliente'] = self.tipo_cliente
        context['id_cliente'] = self.id_cliente

        return context


class EditarPerfilView(core_views.AuthenticatedView):

    template_name = 'cliente/editar_perfil_cliente.html'

    id_cliente = None
    perfil_form = None


    def get(self, request, id_cliente=None, *args, **kwargs):

        self.id_cliente = id_cliente

        perfil = get_list_or_404(models.Perfil.objects.filter(cliente_p=id_cliente).order_by('-id'))[0]

        self.perfil_form = forms.PerfilForm(instance=perfil)

        result = self.render_to_response(self.get_context_data())
        return result


    def post(self, request, id_cliente=None):

        self.id_cliente = id_cliente
        print " id_cliente : %s" %self.id_cliente

        cliente = get_list_or_404(models.Cliente, pk=id_cliente)[0]
        print " el cliente : %s" %cliente.id


        self.perfil_form = forms.PerfilForm(request.POST)

        if self.perfil_form.is_valid():

            self.perfil_form = self.perfil_form.save()

            return redirect('lista_clientes')
        
        else:
            print self.perfil_form.errors

        result = self.render_to_response(self.get_context_data())
        return result


    def get_context_data(self, **kwargs):
        context = super(EditarPerfilView, self).get_context_data(**kwargs)
        context['id_cliente'] = self.id_cliente
        context['perfil_form'] = self.perfil_form

        return context
