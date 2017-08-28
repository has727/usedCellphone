# _*_ encoding: utf-8 _*_

from django.db import models
from datetime import datetime

# Create your models here.

# name = the manufacture's name
# country = the country of origin of the manufacture
class Maker(models.Model):
	name = models.CharField(max_length=10)
	country = models.CharField(max_length=10)
	
	def __str__(self):
		return self.name
	

# maker the foreign key of the Maker
# name = model of the cellphone
# url = the url of cellphone description
class PModel(models.Model):
	maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
	name = models.CharField(max_length=20)
	url = models.URLField(default='https://image.baidu.com/')
	
	def __str__(self):
		return self.name
	

# pmodel = foreign key of the PModel, used to describe the cellphone model
# nickname = description of the cellphone
# description = details of the cellphone
# year = year of production
# price = selling price
class Product(models.Model):
	pmodel = models.ForeignKey(PModel, on_delete=models.CASCADE)
	nickname = models.CharField(max_length=15)
	description = models.TextField(default='No description')
	year = models.PositiveIntegerField(default=2016)
	price = models.PositiveIntegerField(default=0)
	
	def __str__(self):
		return self.nickname
	
	
# product = name of the product
# description = short description of the photo
# url = the url that leads to the photo
class PPhoto(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	description = models.CharField(max_length=20)
	url = models.URLField(default='https://image.baidu.com/')
	
	def __str__(self):
		return self.description


class Test(models.Model):
	MEDIA_CHOICES = (
		('Audio',(
			('vinyl', 'Vinyl'),
			('cd', 'CD'),
			)
		 ),
		('Video', (
			('vhs', 'VHS Tape'),
			('dvd', 'DVD'),
			)
		 ),
		('unknown', 'Unknown'),
	)
	ok = models.CharField(
		max_length=50,
		choices=MEDIA_CHOICES,
		default='Audio',
	)
