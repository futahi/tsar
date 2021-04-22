from django.db import models


class Offers(models.Model):
	primary_key=True
	offer_name= models.CharField(max_length=100)
	offer_image= models.ImageField(upload_to='Services')
	offer_alter= models.CharField(max_length=50)
	offer_desc= models.TextField()
	offer_link= models.CharField(max_length=150, null=True, blank=True)

	def __str__(self):
		return self.offer_name


class Services(models.Model):
	primary_key=True
	service_name= models.CharField(max_length=100)
	service_image= models.ImageField(upload_to='Services')
	service_alter= models.CharField(max_length=50)
	service_desc= models.TextField()
	service_link= models.CharField(max_length=150, null=True, blank=True)

	def __str__(self):
		return self.service_name

class Bottom(models.Model):
    name= models.CharField(max_length=100)
    alter= models.CharField(max_length=100)
    img= models.ImageField(upload_to='Services')
    desc= models.TextField()
    lin= models.CharField(max_length=150, null=True, blank=True)

	# def __str__(self):
	# 	return self.name

class Dost(models.Model):
	primary_key=True
	dost_name= models.CharField(max_length=100)
	dost_image= models.ImageField(upload_to='Services')
	dost_alter= models.CharField(max_length=50)
	dost_desc= models.TextField()
	dost_link= models.CharField(max_length=150, null=True, blank=True)

	def __str__(self):
		return self.dost_name

class City(models.Model):
	primary_key=True
	city_name= models.CharField(max_length=100)
	city_image= models.ImageField(upload_to='Services')
	city_alter= models.CharField(max_length=50)
	city_desc= models.TextField()
	city_link= models.CharField(max_length=150, null=True, blank=True)

	def __str__ (self):
		return self.city_name

class Famous(models.Model):
	primary_key=True
	fame_name= models.CharField(max_length=100)
	fame_image= models.ImageField(upload_to='Services')
	fame_alter= models.CharField(max_length=50)
	fame_desc= models.TextField()
	fame_link= models.CharField(max_length=150, null=True, blank=True)

	def __str__ (self):
		return self.fame_name





class Last(models.Model):
	primary_key=True
	last_name= models.CharField(max_length=100)
	last_image= models.ImageField(upload_to='Services', null=True, blank=True )
	last_file= models.FileField(upload_to='Services', null=True, blank=True)
	last_alter= models.CharField(max_length=50)
	last_desc= models.TextField(null=True, blank=True)
	last_link1=models.URLField(max_length=200, null=True, blank=True)
	last_link2=models.URLField(max_length=200, null=True, blank=True)
	last_reference= models.TextField(null=True, blank=True)

	def __str__(self):
		return self.last_name



