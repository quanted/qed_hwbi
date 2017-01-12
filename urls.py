"""
Definition of urls for qed_hwbi.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views


from hwbi_app import views
from hwbi_app import algorithms
from hwbi_app import description
from hwbi_app import input
from hwbi_app import links_left
from hwbi_app import map
from hwbi_app import references


urlpatterns = [
    # Examples:
    #url(r'^hwbi', views.hwbi_view),    
    #url(r'^$', description.description_page, {'model': "hwbi"}),
    url(r'^hwbi$', description.description_page, {'model': "hwbi"}),
    url(r'^hwbi/input$', input.input_page, {'model': "hwbi"}),
    url(r'^hwbi/map$', map.map_page, {'model': "hwbi"}),
    url(r'^hwbi/algorithms$', algorithms.algorithm_page, {'model': "hwbi"}),
    url(r'^hwbi/references$', references.references_page, {'model': "hwbi"}),
    #url(r'^$', app.views.home, name='home'),
    #url(r'^contact$', app.views.contact, name='contact'),
    #url(r'^about', app.views.about, name='about'),
    #url(r'^login/$',
    #    django.contrib.auth.views.login,
    #    {
    #        'template_name': 'app/login.html',
    #        'authentication_form': app.forms.BootstrapAuthenticationForm,
    #        'extra_context':
    #       {
    #            'title': 'Log in',
    #            'year': datetime.now().year,
    #       }
    #    },
    #    name='login'),
    #url(r'^logout$',
    #    django.contrib.auth.views.logout,
    #    {
    #        'next_page': '/',
    #    },
    #    name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
