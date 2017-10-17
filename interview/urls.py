from django.conf.urls import url
from django.contrib import admin
from int_order.views import OrderViewSet
from int_user_info.views import ScoresViewSet
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns_order = [
    url('^api/orders/(?P<pk>\d+)/$', OrderViewSet.as_view({'patch': 'partial_update', 'get': 'retrieve'})),
    url('^api/orders/$', OrderViewSet.as_view({'get': 'list'}))
]

urlpatterns_user_info = [
    url('^api/scores/$', ScoresViewSet.as_view({'get': 'list'}))
]

urlpatterns_index = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
]

urlpatterns += urlpatterns_order
urlpatterns += urlpatterns_index
urlpatterns += urlpatterns_user_info
