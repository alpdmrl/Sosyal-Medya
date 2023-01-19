from django.urls import path
from .views import *

urlpatterns = [
    path('register/', userRegister, name='register'),
    path('login/', userLogin, name='login'),
    path('logout/', userLogout, name='logout'),
    path('profil/', profil, name='profil'),
    path('update/', update, name='update' ),
    path('reset/', sifre, name='sifre'),
    path('other/<str:pk>', userProfil, name='userProfil')
]