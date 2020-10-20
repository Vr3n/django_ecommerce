from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Distributor)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(OrderStatus)
admin.site.register(PaymentType)
admin.site.register(Order)
admin.site.register(Cart)