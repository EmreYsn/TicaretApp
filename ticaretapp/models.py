from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ticaret(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"Username= {self.username}"