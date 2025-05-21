from django.contrib import admin
from .models import Customer, Item, ItemPurchase, Transaction
# Register your models here.

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(ItemPurchase)
admin.site.register(Transaction)