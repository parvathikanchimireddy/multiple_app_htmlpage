from app1.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('parvathi/',parvathi,name='parvathi'),
]