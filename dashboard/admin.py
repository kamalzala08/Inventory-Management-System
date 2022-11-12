from django.contrib import admin
from .models import Product,Order
# Register your models here.

admin.site.site_header ="kamal zala"

class ProductDisplay(admin.ModelAdmin):
      list_display    = ['id','name','category','quantity']
      list_filter = ['category']
      


class OrderDisplay(admin.ModelAdmin):
    list_display    = ['id','product','orderby','order_quantity','date']
    list_filter = ['product','date']
      
admin.site.register(Product,ProductDisplay)   
admin.site.register(Order,OrderDisplay)                                                                                                                                                                    