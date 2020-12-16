from django.urls import path,include
from . import views

from rest_framework.urlpatterns import format_suffix_patterns
from .views import PortfolioView
from django.conf import settings
from django.conf.urls.static import static
app_name = "main"



PortfolioView_list = PortfolioView.as_view({
    'post': 'create',
    'get': 'list'
})
PortfolioView_detail = PortfolioView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('portfolio/', PortfolioView_list, name='PortfolioView_list'),
    path('portfolio/<int:pk>/', PortfolioView_detail, name='PortfolioView_detail'),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
])



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)