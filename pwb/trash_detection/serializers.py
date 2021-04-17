from rest_framework import serializers
#from django.forms.fields import ImageField
class TrashDetectionSerializer(serializers.Serializer):
    boxes = serializers.DictField()
    image = serializers.ImageField()
    