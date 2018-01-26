from django.shortcuts import redirect
from django import http
from django.utils import simplejson as json
# Create your views here.
from django.conf import settings
import datetime
from django.views.generic import TemplateView, View

class AuthenticatedView(TemplateView):
    """Class for a view with login required"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect(settings.LOGIN_URL)
            

        return super(AuthenticatedView, self).dispatch(request,
                *args, **kwargs)

class JSONResponseMixin(object):
    """Class for a view thats only response in json format"""

    @classmethod
    def get_json_response(cls, content, **httpresponse_kwargs):
        """Construct a 'HttpResponse' object"""
        return http.HttpResponse(content, content_type='application/json',
                                 **httpresponse_kwargs)

    @classmethod
    def convert_context_to_json(cls, context):
        """Convert the context dictionary into a JSON object"""
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        if context:
            return json.dumps(context)
        else:
            return ''

    def render_to_response(self, context):
        """Returns a JSON response containing 'context' as payload"""
        return self.get_json_response(self.convert_context_to_json(context))





class HomePageView(AuthenticatedView):
    template_name = 'core/principal.html'


