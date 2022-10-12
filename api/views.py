from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
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

class HWSV(APIView):
	def post(self, request):
		data = request.data
		print('request.data')
		print(data)
		
