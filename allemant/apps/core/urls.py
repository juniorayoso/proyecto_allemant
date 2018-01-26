from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from apps.core import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'allemant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^home/', views.HomePageView.as_view(),name='home'),
    
    

)
