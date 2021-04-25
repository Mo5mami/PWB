from .base import *

DEBUG = False

#TORCHSERVE_URL = "https://torchservemo5.azurewebsites.net/"
TORCHSERVE_URL ="http://54.162.113.184/"
"""ALLOWED_HOSTS = [
    "https://personalwebsitemo5.vercel.app",
    "http://127.0.0.1:3000/"
]"""

ALLOWED_HOSTS = [r'*']

CORS_ALLOWED_ORIGINS = [
    "https://personalwebsitemo5.vercel.app",
    "http://127.0.0.1:3000"
]
CORS_ALLOW_ALL_ORIGINS = False

WSGI_APPLICATION = 'pwb.wsgi.prod.application'
