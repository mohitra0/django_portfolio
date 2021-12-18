from django.contrib import admin

from .models import ProductConfig, Offer

# Register your models here.
class OfferAdmin(admin.ModelAdmin):
    list_display=('code','description','discount')


class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')


admin.site.register(ProductConfig,ProductAdmin)
admin.site.register(Offer,OfferAdmin)

