from django.contrib.auth import get_user_model
from django.db import models
# Create your models here.

User = get_user_model()

class Programmer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pass

