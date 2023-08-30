from django.db import models
from datetime import datetime

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=230,default = ' ' )
    page = models.IntegerField(default= 250)

    def __str__(self) -> str:
        return self.name
    
class Article(models.Model):
    name = models.CharField(max_length=230,default = ' ' )
    page = models.IntegerField(default= 250)
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.name 
    
