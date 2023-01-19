from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('olustur/', olustur, name='olustur'),
    path('kesfet/', kesfet, name='kesfet')
]