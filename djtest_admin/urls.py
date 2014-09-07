from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from djtest_admin.views import hello

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djtest_admin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^hello/', hello),
	
    url(r'^login/', include('login.urls')), #login* ?
	url(r'^login1/', include('login.urls')), #login* ?
)
