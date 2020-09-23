from django.db import models
from django.urls import reverse


class Client(models.Model):
    name=models.CharField(max_length=64)
    def __str__(self):
        return self.name
# Create your models here.
class Position(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    company=models.ForeignKey(Client,on_delete=models.CASCADE)
    name=models.CharField(max_length=64)
    location=models.CharField(max_length=64,null=True)
    account_manager=models.CharField(max_length=128,null=True)
    tips=models.TextField(default=None,blank=True,null=True)
    description=models.TextField(default=None,blank=True,null=True)
    file=models.FileField(blank=True)
    def __str__(self):
        return(str(self.id)+' - '+self.company.name+' '+self.name)  
    # def get_absolute_url(self):
    #     return reverse('positions:position-detail',kwargs={'id':self.id})