from django.contrib import admin
from .models import Order, OrderItem

admin.sites.AdminSite.site_header = 'Sabz Shop administration'
admin.sites.AdminSite.site_title = "panel"
admin.sites.AdminSite.index_title = "Admin panel"


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 0
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'address', 'postal_code', 'province', 'city', 'created',
                    'updated', 'paid', 'buyer']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInLine]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product']
