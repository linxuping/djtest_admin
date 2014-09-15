from django.db import models

# Create your models here.
class Task(models.Model):  
    class Meta:  
        permissions = (  
            ('oprater_task','try this perm ~'),  
        )  
        
# Create your models here.
class Task2(models.Model):  
    class Meta:  
        permissions = (  
            ('oprater_task2','try this perm2 ~'),  
        )  