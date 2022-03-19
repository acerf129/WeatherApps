from django.urls import path,include
from . import views
#urlpatterns

urlpatterns=[
    path('',views.index,name='index')
]