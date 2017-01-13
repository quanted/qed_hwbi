from django.conf.urls import include, url

#regular expressions
# the r in r'^cts/index.html$' indicates that what is inside the quotes is a regular expression
# the ^ in r'^cts/index.html$' indicates that we are looking to extend from the root dir from this part of the string
# the $ in r'^cts/index.html$' indicates that we are looking to extend end the mathing part exactly here

print('qud_hwbi.urls')
#appends to the list of url patterns to check against
urlpatterns = [
    url(r'^hwbi/', include('hwbi_app.urls')),
]