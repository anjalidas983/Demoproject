from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_name=models.CharField(max_length=20)
    description=models.CharField(max_length=100)
    img=models.ImageField(upload_to='Movies/img',null=True,blank=True)
    def __str__(self):
         return self.movie_name