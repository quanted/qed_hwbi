"""
Definition of urls for qed_hwbi.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

#import app.forms
#import app.views
import hwbi_app.views
import hwbi_app.views.algorithms
import hwbi_app.views.description
import hwbi_app.views.input
import hwbi_app.views.links_left
import hwbi_app.views.map
import hwbi_app.views.references


# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^hwbi', hwbi_app.views.hwbi_view),
    url(r'^$', description.description_page, {'model': "hwbi"}),
    url(r'^description$', description.description_page, {'model': "hwbi"}),
    url(r'^input$', input.input_page, {'model': "hwbi"}),
    url(r'^map$', map.map_page, {'model': "hwbi"}),
    url(r'^algorithms$', algorithms.algorithm_page, {'model': "hwbi"}),
    url(r'^references$', references.references_page, {'model': "hwbi"}),
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
