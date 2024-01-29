from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from . import views

urlpatterns = [   
    path("",views.index,name="drawing_list"),
    path("upload_pdf/",views.upload_pdf,name='upload_pdf'),
    path("upload_design/",views.upload_design,name='upload_design'),
    path("update_design/<int:id>/",views.update_design,name='update_design'),
    path("delete_design/<int:pk>/",views.delete_design,name='delete_design'),   
    
]