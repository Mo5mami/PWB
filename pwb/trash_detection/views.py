from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .trash_detection_service import TrashDetectionService
from asgiref.sync import sync_to_async
import asyncio

"""class TrashDetection(APIView):
    
    def post(self, request, format=None):
    
        print("am I async : ",asyncio.iscoroutinefunction(self.post))
        async_fn = sync_to_async(TrashDetectionService.inference,thread_sensitive=False)
        return  async_fn(request)"""

@api_view([ 'POST'])
def trash_detection(request):
    if request.method == 'POST':
        return TrashDetectionService.inference(request)


    
        