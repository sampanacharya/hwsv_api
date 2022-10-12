from django.urls import path, include
from django.conf.urls import url 
from .views import HWSV

urlpatterns = [
	path('predict/',HWSV.as_view(),name='hwsv'),
]