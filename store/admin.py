from django.contrib import admin
from .models import Category, Product, Order, OrderItem, ShippingAddress
from .define import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub_category', 'is_sub')
    list_filter = ["name", "sub_category", "is_sub"]
    search_fields = ["name"]
    #prepopulated_fields = {'slug': ('name',)}
    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS

class Products(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ['name', 'price']
    search_fields = ["name"]
    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)