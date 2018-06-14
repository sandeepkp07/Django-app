from django.db import models
from django.db import models

class Adding(models.Model):
        Name = models.CharField(max_length=100)
	Marks = models.CharField(max_length=100)
	userid = models.CharField(max_length=120,blank=False)

	def __unicode__(self):
		return self.Name
class Tweet(models.Model):
	fullname = models.CharField(max_length=120,blank=False)
	tweetcount = models.CharField(max_length=100)

class Convert(models.Model):
	status=(('INR','INR'),
		("USD",'USD'),
		("EUR",'EUR'),
		("GBP",'GBP'),
		('IDR','IDR'),
		('BGN','BGN'),
		('ILS','ILS'),
		('AED','AED'),
		('HKD','HKD'),
		("SGD",'SGD'))
	convert_from = models.CharField(
		choices=status,
		max_length=3,
		blank = False,
		default='INR',

	)
	convert_to = models.CharField(
		choices=status,
		max_length=3,
		default='USD',
    	blank = False,
    	)
        #amount = models.IntegerField(blank= False)

	def __unicode__(self):
		return self.convert_from


class Reader(models.Model):
	url = models.CharField(max_length=120,blank=False)

class Chat(models.Model):
	message = models.CharField(max_length=250,blank=False)




# Create your models here.
# Create your models here.
