from rest_framework import generics

from item_app.models import Items
from item_app.serializers import ItemSerializer


class ItemsList(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer


class ItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
