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

		
class ImageViewSet(APIView):
	queryset = UploadImageTest.objects.all()
	serializer_class = ImageSerializer

	def post(self, request):
		
		# original image
		org = np.asarray(bytearray(request.FILES['original'].read()), dtype="uint8") 
		org = cv2.imdecode(org, cv2.IMREAD_COLOR)
		org = cv2.resize(org, (220, 155))
		org = cv2.bitwise_not(org)
		org = org / 255
		org = np.expand_dims(org, axis=0)

		# forged image
		forg = np.asarray(bytearray(request.FILES['forged'].read()), dtype="uint8") 
		forg = cv2.imdecode(forg, cv2.IMREAD_COLOR)
		
		forg = cv2.resize(forg, (220, 155))
		forg = cv2.bitwise_not(forg)
		forg = forg/255
		forg = np.expand_dims(forg, axis=0)

		print(org.shape, forg.shape)
		mod = ApiConfig.model

		assert(len(org.shape) == 4 and len(forg.shape) == 4),"Invalid Shape"
		return Response({'score': mod.predict([org, forg],3)[0][0]},status=200)
	