from django.db import models

# Create your models here.
class Product(models.Model):
    title= models.CharField(max_length= 80)
    image= models.ImageField(upload_to= 'media', null=True, blank=True) #upload to media folder 
    description= models.CharField(max_length= 250)
    price= models.DecimalField(decimal_places= 2, max_digits= 6)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url= self.image.url 
        except:
            url=''
        return url