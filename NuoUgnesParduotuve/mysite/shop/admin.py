from django.contrib import admin
from .models import *

class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 0

class OrderInline(admin.TabularInline):
    model = Order
    extra = 0

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    inlines = [OrderInline]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    inlines = [OrderLineInline]

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date_ordered', 'status')
    list_filter = ('status',)
    search_fields = ('id', 'customer', 'date_ordered')
    list_editable = ('status',)

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'date_added')

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'address', 'date_added')
    list_filter = ('customer', 'order')

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
