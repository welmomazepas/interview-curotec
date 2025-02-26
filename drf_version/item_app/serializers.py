from rest_framework import serializers

from item_app.models import Items


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['id', 'name', 'description', 'price']
