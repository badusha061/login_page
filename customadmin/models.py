from django.db import models



class CustomUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username
    
    
