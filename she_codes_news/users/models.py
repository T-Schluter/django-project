#from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    #this is where I would put custom fields



    def __str__(self):
        return self.username


