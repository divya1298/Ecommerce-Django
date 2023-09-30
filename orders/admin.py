from django.contrib import admin
from .models import Payments, Order, OrderProduct



# Register your models here.
admin.site.register(Payments)
admin.site.register(Order)
admin.site.register(OrderProduct)