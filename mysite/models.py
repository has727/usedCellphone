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
	url = models.URLField(default='https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=iphone&step_word=&hs=0&pn=9&spn=0&di=127863767020&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=2103764748%2C456254565&os=3803373560%2C1675667030&simid=4255193451%2C548934275&adpicid=0&lpn=0&ln=1970&fr=&fmq=1503845799788_R&fm=detail&ic=0&s=undefined&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2F4493bz.1985t.com%2Fuploads%2Fallimg%2F150108%2F4-15010Q60931.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fktzit_z%26e3B99ln_z%26e3Bv54AzdH3Ft4w2jAzdH3F0lcn_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0')
	
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
	url = models.URLField(default='https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=iphone&step_word=&hs=0&pn=12&spn=0&di=4008368210&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=1536525877%2C2795221932&os=2086730783%2C1215546982&simid=3311443299%2C149445111&adpicid=0&lpn=0&ln=1970&fr=&fmq=1503845799788_R&fm=detail&ic=0&s=undefined&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fimg.pconline.com.cn%2Fimages%2Fproduct%2F5686%2F568697%2F3.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Brv5gstgj_z%26e3Bv54_z%26e3BvgAzdH3F4w6hjpAzdH3F09aAzdH3F09am9aa_z%26e3Bip4s%3Fqq-ru-p5%3Drvqq_z%26e3Bvdv&gsm=0&rpstart=0&rpnum=0')
	
	def __str__(self):
		return self.description

