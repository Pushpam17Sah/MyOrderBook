from django.urls import path,include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('admin', views.AdminModelViewSet)
router.register('supplier', views.SupplierModelViewSet)
router.register('item', views.ItemModelViewSet)


urlpatterns = [
    path('',include(router.urls)),
]

#test
