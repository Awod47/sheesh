from django.db import models

# Create your models here.
class Newsletter(models.Model):
	name 	= models.CharField(max_length = 30)
	email 	= models.EmailField()
	date 	= models.DateTimeField(auto_now_add= True, blank= True)