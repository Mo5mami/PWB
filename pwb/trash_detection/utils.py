import base64
from django.conf import settings
# Create your views here.


class FixFormat:
    
    @classmethod
    def string_to_base64(cls , s):
        return base64.b64encode(s.encode('utf-8'))

    @classmethod
    def byte_to_base64(cls , b):
        return base64.b64encode(b)
    
    @classmethod
    def base64_to_byte(cls , b):
        return base64.b64decode(b)

    @classmethod
    def base64_to_string(cls , b):
        return base64.b64decode(b).decode('utf-8')

    @classmethod
    def byte_to_string(cls , b):
        return base64.b64encode(b).decode('utf-8')