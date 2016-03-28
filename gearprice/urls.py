from django.conf.urls import patterns, include, url
from gearprice.apps.price_history.api import GearResource, AlarmResource
from tastypie.api import Api


from django.contrib import admin
admin.autodiscover()

#
#
# API configuration
v1_api = Api(api_name='v1')
v1_api.register(GearResource())
v1_api.register(AlarmResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gearprice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'gearprice.apps.price_history.views.index', name='home'),
    url(r'^gear/([0-9]+)/$', 'gearprice.apps.price_history.views.show', name='gear.show'),
    url(r'^gear/([0-9]+)/partial/$', 'gearprice.apps.price_history.views.content_partial', name='gear.content_partial'),
    url(r'^gear/([0-9]+)/alarm/$', 'gearprice.apps.price_history.views.new_alarm', name='gear.new_alarm'),

    url(r'^tester$', 'gearprice.apps.price_history.views.xpath_tester', name='tester'),
    url(r'^update$', 'gearprice.apps.price_history.views.get_prices', name='get_prices'),

    #
    #
    # API url confs
    (r'^api/', include(v1_api.urls)),
)
