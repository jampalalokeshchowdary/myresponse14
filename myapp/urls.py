from django.urls import path
from .views import *
app_name='myapp'

urlpatterns=[
    path('',app,name='app'),
    path('courses/',courses,name='courses'),
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('signin/',signin,name='signin'),
    path('requestcall/',requestcall,name='requestcall'),
    path('signin/login/',login,name='login'),
]