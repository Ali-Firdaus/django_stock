from django.db import models

# Create your models here.
class companies(models.Model):
	Symbol=models.CharField(max_length=10)
	Company_Name=models.CharField(max_length=10)
	Halal_Category=models.CharField(max_length=10)
	def __str__(self):
		return self.Symbol