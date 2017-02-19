from __future__ import unicode_literals

from django.db import models

# Create your models here.
class mobile(models.Model):
	title=models.TextField(max_length=800)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	avalable=models.TextField(max_length=500)
	info=models.TextField(max_length=10000)
	url=models.TextField(max_length=10000)
	
	def __str__(self):
		return self.title