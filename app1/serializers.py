from rest_framework import serializers
from .models import Admin,Supplier,Item

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields="__all__"

class SupplierSerializer(serializers.ModelSerializer):
    items=serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model=Supplier
        fields=['id','name','phone_no','whatsapp','email','shop_name','admin_id','items']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields=['id','item_name','date_added','upload_image','status','supplier_id']