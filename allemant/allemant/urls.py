from django.conf.urls import patterns, include, url

from django.conf import settings

from django.conf.urls.static import static

from django.contrib import admin
 
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'allemant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^core/', include('apps.core.urls')),
    url(r'^cliente/', include('apps.cliente.urls')),
    url(r'^poliza/', include('apps.poliza.urls')),

    url(r'^administrativo/', include('apps.administrativo.urls')),

    url(r'^login$', 'django.contrib.auth.views.login',
            {'template_name': 'core/login.html'},name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login',
            name='logout'),

    # ========= media arcivos poliza ===============================
    url(r'^allemant/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    # ==============================================================

)
