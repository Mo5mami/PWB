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

class TrashDetectionService:
    
    @classmethod
    def trash_detection_inference_url(cls , ):
        return os.path.join(settings.TORCHSERVE_URL , "predictions/trash_detection")

    @classmethod
    def trash_detection_request(cls , data):

        inference_url = TrashDetectionService.trash_detection_inference_url()
        response = requests.post(inference_url,data=data["data"] , files=data["files"])
        #return response
        #print("response content : ",response.content)
        """prediction = json.loads(response.content.decode())
        prediction["image"] = ImageFile(io.BytesIO(FixFormat.base64_to_byte(prediction["image"])) , name="result.png")
        print("prediction keys : ",prediction.keys())
        pred_serializer = TrashDetectionSerializer(data = prediction)
        if pred_serializer.is_valid():
            return Response(pred_serializer.data,status=response.status_code,)
        else :
            print("errors : ",pred_serializer.errors)
        return Response({"errors" : "ERROR"},status=response.status_code,)"""
        prediction = json.loads(response.content.decode())
        return Response(prediction,status=response.status_code,)

    @classmethod
    def inference(cls , request):
        print("request : ",request)
        print("request data : ",request.data)
        query = {}
        #query["data"] = request.data
        #query["files"] = {"image" : request.FILES["image"].read()}
        query["data"] = {"return_image" : True}
        query["files"] = {"image" : request.data["file"].read()}
        
        print("file type : ",type(query["files"]["image"]))
        print("file length : ",len(query["files"]["image"]))
        response = TrashDetectionService.trash_detection_request(query)
        return response 
        #return Response("hi",)
