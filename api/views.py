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

import matplotlib.pyplot as plt 
import matplotlib


		
class ImageViewSet(APIView):
	queryset = UploadImageTest.objects.all()
	serializer_class = ImageSerializer

	def post(self, request):
		
		org = cv2.imdecode(np.fromstring(request.FILES['original'].read(), np.uint8), cv2.IMREAD_UNCHANGED)	
		forg = cv2.imdecode(np.fromstring(request.FILES['forged'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
		print(org.shape, forg.shape)
		# original image
		org = cv2.resize(org, (220, 155))
		org = cv2.bitwise_not(org)
		org = org / 255
		org = np.expand_dims(org, axis=0)

		# forged image
		forg = cv2.resize(forg, (220, 155))
		forg = cv2.bitwise_not(forg)
		forg = forg/255
		forg = np.expand_dims(forg, axis=0)

		print(org.shape, forg.shape)
		mod = ApiConfig.model

		assert(len(org.shape) == 4 and len(forg.shape) == 4),"Invalid Shape"
		return Response({'score': mod.predict([org, forg])
						})