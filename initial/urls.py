from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name='index'),
    path("",views.index0,name="index0"),
    
]