from rest_framework.response import Response
from .models import Motabari3
from rest_framework import filters
from .serializers import Motabari3Serializer
from rest_framework import viewsets,generics


class Motabare3Viewset(viewsets.ModelViewSet):
    
    queryset = Motabari3.objects.all()
    serializer_class = Motabari3Serializer
    def update(self, request, *args, **kwargs):
        return Response({"response":"method not allowed"})
    def destroy(self, request, *args, **kwargs):
        return Response({"response":"method not allowed"})
    
class Motabari3ListView(generics.ListAPIView):
    queryset = Motabari3.objects.all()
    serializer_class = Motabari3Serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['wilaya','commun','zomra']
