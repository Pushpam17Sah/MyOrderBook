from rest_framework import serializers
from .models import Admin,Supplier,Item

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields="__all__"

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supplier
        fields="__all__"

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields="__all__"