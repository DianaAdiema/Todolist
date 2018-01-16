from django.conf.urls import url

from django.urls import  path, re_path
from . import views

urlpatterns = [
    
     path('', views.index, name='index'),
	 path('todo/details/<id>/', views.details),
     #re_path('details/(?P<int:id>)/', views.details),
    
]