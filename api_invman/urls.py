from django.conf.urls import patterns, url, include
from rest_framework import routers
import api
import views

router = routers.DefaultRouter()
router.register(r'api', api.apiViewSet)


urlpatterns = patterns('',
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += patterns('',
    # urls for api
    url(r'^api_invman/api/$', views.apiListView.as_view(), name='api_invman_api_list'),
    url(r'^api_invman/api/create/$', views.apiCreateView.as_view(), name='api_invman_api_create'),
    url(r'^api_invman/api/detail/(?P<id>\S+)/$', views.apiDetailView.as_view(), name='api_invman_api_detail'),
    url(r'^api_invman/api/update/(?P<id>\S+)/$', views.apiUpdateView.as_view(), name='api_invman_api_update'),
)

