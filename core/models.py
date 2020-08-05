from django.db import models

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=31)
	description = models.CharField(max_length = 255)
	color = models.CharField(max_length = 7)
	href = models.CharField(max_length = 31)

	def __str__(self):
		return self.name
