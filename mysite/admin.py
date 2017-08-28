from django.contrib import admin
from mysite.models import Maker, Product, PModel, PPhoto, Test

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ('pmodel', 'nickname', 'price', 'year')
	search_fields = ('nickname',)
	ordering = ('price', 'year',)
	
	
class PModelAdmin(admin.ModelAdmin):
	list_display = ('maker', 'name', 'url')
	
	
admin.site.register(Maker)
admin.site.register(PPhoto)
admin.site.register(Product, ProductAdmin)
admin.site.register(PModel, PModelAdmin)
admin.site.register(Test)
