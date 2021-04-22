from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .trash_detection_service import TrashDetectionService
from asgiref.sync import sync_to_async

class TrashDetection(APIView):
    async def __call__():
        pass 
        
    def post(self, request, format=None):
        """
        Demand inference on the object detection model
        """
        return TrashDetectionService.inference(request)
    
        