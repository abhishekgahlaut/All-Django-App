from django.db import models

from auditable.models import Auditable
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Casino(Auditable):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=255)
	# price = models.IntegerField(default=1, validators=[MaxValueValidator(220), MinValueValidator(1)])
	price = models.IntegerField(default=1) 


	def __str__(self):
		return self.name
	


