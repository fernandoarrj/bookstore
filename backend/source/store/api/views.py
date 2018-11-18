from .serializers import StoreSerializer

from rest_framework import viewsets

from store.models import Store

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
