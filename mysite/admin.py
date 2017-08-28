from django.contrib import admin
from mysite.models import Maker, Product, PModel, PPhoto

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ('pmodel', 'nickname', 'price', 'year', 'description')
	
	
admin.site.register(Maker)
admin.site.register(PPhoto)
admin.site.register(Product, ProductAdmin)
admin.site.register(PModel)
