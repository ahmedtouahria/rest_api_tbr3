from django.urls import include, path
from .views import Motabare3Viewset , Motabari3ListView
from rest_framework import routers

router = routers.DefaultRouter()

router.register('motabari3',Motabare3Viewset)


urlpatterns = [
    path('motaber3s/',include(router.urls)),
    path('',Motabari3ListView.as_view()),
    
    
]
