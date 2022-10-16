from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response 
from rest_framework import status
from .apps import ApiConfig

# for pre processing 
import cv2
import numpy as np
from tensorflow import keras

import json
from django.http import QueryDict
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import UploadImageTest
from .serializer import ImageSerializer

class HWSV(APIView):
	def post(self, request):
		data = request.data
		print('request.data')
		print(data)
		
class ImageViewSet(ListAPIView):
	queryset = UploadImageTest.objects.all()
	serializer_class = ImageSerializer

	def post(self, request):
		form_data = {'name':''} 
		success = True 
		response = []
		for (name,images) in zip(request.FILES.getlist('name'),request.FILES.getlist('images')):
			form_data['name'] = name
			form_data['images'] = images
			imgSerial = ImageSerializer(name=form_data['name'],image=images)
			print(name, images)
			if(imgSerial.is_valid()):
				imgSerial.save()
				response.append(imgSerial.data)
			else:
				success = False
		if success:
			return Response({
				'status':1,
				'message':'success',
				'data':form_data['name'],
				})
		return Response({
			'status':0,
			'message':'error!',
			})