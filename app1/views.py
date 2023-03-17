from rest_framework import viewsets
from .serializers import AdminSerializer,SupplierSerializer,ItemSerializer
from .models import Admin,Supplier,Item
# Create your views here.

class AdminModelViewSet(viewsets.ModelViewSet):
    queryset=Admin.objects.all()
    serializer_class=AdminSerializer

class SupplierModelViewSet(viewsets.ModelViewSet):
    queryset=Supplier.objects.all()
    serializer_class=SupplierSerializer

class ItemModelViewSet(viewsets.ModelViewSet):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer
