from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from views import PartCreateView, PartListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'))
    url(r'^create$', PartCreateView.as_view(), name='part_create'),
    url(r'^list$', PartListView.as_view(), name='part_list'),

)
