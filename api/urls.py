from django.urls import path, include
from django.conf.urls import url 
from .views import *

urlpatterns = [
	path('predict/',HWSV.as_view(),name='hwsv'),
	path('upload/',ImageViewSet.as_view())
]