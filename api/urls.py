from django.urls import path, include
from django.conf.urls import url 
from .views import HWSV, ImageViewSet

urlpatterns = [
	path('predict/',HWSV.as_view(),name='hwsv'),
	path('upload/',ImageViewSet.as_view(), name = 'upload'),
]