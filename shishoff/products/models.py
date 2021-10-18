from django.db import models

# Create your models here.
class Product(models.Model):
    Title= models.CharField(max_length= 80)
    Image= models.ImageField(upload_to= 'media') #upload to media folder 
    Description= models.CharField(max_length= 250)
    Price= models.DecimalField(decimal_places= 2, max_digits= 6)
    date = models.DateTimeField(auto_now_add=True)
