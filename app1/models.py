from django.db import models

# Create your models here.
class Admin(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self) :
        return self.name


class Supplier(models.Model):
    name=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=15)
    whatsapp=models.CharField(max_length=15,blank=True,null=True)
    email=models.EmailField(max_length=254,blank=True,null=True)
    shop_name=models.CharField(max_length=30,blank=True,null=True)
    admin_id=models.ForeignKey(Admin,on_delete=models.CASCADE,related_name='admin')

    def __str__(self) :
        return self.name



class Item(models.Model):
    item_name=models.CharField(max_length=30)
    date_added=models.DateTimeField(auto_now=True,editable=False)
    upload_image=models.ImageField(blank=True,null=True)
    status = models.BooleanField(default=False)
    # admin_id=models.ForeignKey(Admin,on_delete=models.CASCADE)
    supplier_id=models.ForeignKey(Supplier,on_delete=models.CASCADE,related_name='items')
    # supplier_id=models.OneToOneField(Supplier,on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name
