from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BigDataView

app_name = "parsed_data"

BigDataView_list = BigDataView.as_view({
    'post': 'create',
    'get': 'list'
})
BigDataView_detail = BigDataView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('bigdata/', BigDataView_list, name='PortfolioView_list'),
    path('', views.data, name='data'),
    path('bigdata/<int:pk>/', BigDataView_detail, name='PortfolioView_detail'),
])
