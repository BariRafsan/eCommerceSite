from django.contrib import admin
from .models import Product, Customer,Cart,Order

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'price', 'description','category', 'image']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'phone','password']    


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'product', 'quantity']

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'product', 'quantity','total_cost','ordered_date']