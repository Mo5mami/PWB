from django.conf import settings
import os
import io
import requests
from rest_framework.response import Response
import json 
from .utils import FixFormat
from .serializers import TrashDetectionSerializer
from django.core.files import File 
from django.core.files.images import ImageFile 
from asgiref.sync import sync_to_async

class TrashDetectionService:
    
    
    @classmethod
    def trash_detection_inference_url(cls , ):
        return os.path.join(settings.TORCHSERVE_URL , "predictions/trash_detection")

    
    @classmethod
    def trash_detection_request(cls , data):

        inference_url = TrashDetectionService.trash_detection_inference_url()
        response = requests.post(inference_url,data=data["data"] , files=data["files"])
        prediction = json.loads(response.content.decode())
        return Response(prediction,status=response.status_code,)

    
    @classmethod
    def inference(cls , request):
        print("request : ",request)
        print("request data : ",request.data)
        query = {}
        query["data"] = {"return_image" : True}
        query["files"] = {"image" : request.data["file"].read()}
        print("file type : ",type(query["files"]["image"]))
        print("file length : ",len(query["files"]["image"]))
        response = TrashDetectionService.trash_detection_request(query)
        return response 
        
