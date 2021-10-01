from django.db import models

# Create your models here.
class subscribe(models.Model):
    Name= models.CharField(max_length= 50)
    Email= models.EmailField()
    date= models.DateTimeField(auto_now_add= True, blank= True)
