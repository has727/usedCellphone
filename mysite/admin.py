from django.contrib import admin
from mysite.models import Maker, Product, PModel, PPhoto

# Register your models here.

admin.site.register(Maker)
admin.site.register(PPhoto)
admin.site.register(Product)
admin.site.register(PModel)
