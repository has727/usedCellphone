from django.shortcuts import render, HttpResponse
from .models import PModel, Product, PPhoto, Maker
from django.template.loader import get_template

# Create your views here.

def index(request):
	templates = get_template('index.html')
	products = Product.objects.all()
	html = templates.render(locals())
	return HttpResponse(html)


def detail(request, id):
	try:
		product = Product.objects.get(id=id)
		images = PPhoto.objects.filter(product=product)
	except:
		pass
	templates = get_template('detail.html')
	html = templates.render(locals())
	return HttpResponse(html)