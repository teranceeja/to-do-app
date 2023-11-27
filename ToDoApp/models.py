from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class ToTable(models.Model):
    userName = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(blank=True,null=True)
    dateAdded = models.DateTimeField(auto_now_add=True)
    todo_id = models.IntegerField(primary_key=True)
    
    
    def __str__(self):
        return self.title


