#from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass
    this is where I would put custom fields
    author = models.ForeignKey(
         get_user_model(),
         on_delete=models.CASCADE
    )
    
    pub_date = models.DateTimeField()
    content = models.TextField()


    def __str__(self):
        return self.username


