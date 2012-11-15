from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       (r'^create_page?/$', 'labgeeks_pythia.views.edit_page'),
                       (r'^(?P<slug>[-\w]+)/edit/$', 'labgeeks_pythia.views.edit_page'),
                       (r'^(?P<slug>[-\w]+)/save/$', 'labgeeks_pythia.views.edit_page'),
                       (r'^(?P<slug>[-\w]+)/$', 'labgeeks_pythia.views.view_page'),
                       (r'^(?P<slug>[-\w]+)/revisions/$', 'labgeeks_pythia.views.revision_history'),
                       (r'^(?P<slug>[-\w]+)/select_revision/$', 'labgeeks_pythia.views.select_revision'),
                       (r'^$', 'labgeeks_pythia.views.pythia_home'),
                       )
