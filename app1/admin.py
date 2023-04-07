from django.contrib import admin
from . models import Admin,Supplier,Item

# Register your models here.
@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display=['id','name','phone_no','whatsapp','email','shop_name','admin_id']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=['id','item_name','date_added','upload_image','status','supplier_id']