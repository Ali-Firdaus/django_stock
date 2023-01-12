from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

# Create your models here.
class Stock(models.Model):
	ticker=models.CharField(max_length=10)
	owner = models.ForeignKey(User, on_delete= models.CASCADE)
	Halal=models.CharField(max_length=10)

	def __str__(self):
		return self.ticker