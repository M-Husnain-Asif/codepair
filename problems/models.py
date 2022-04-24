
from djongo import models
# from mongoengine import Document,models

# Create your models here.
class Problems(models.Model):
    title= models.TextField(max_length=200)
    desc = models.TextField(max_length=500)
    complexity = models.TextField(max_length=30)
    domain = models.TextField(max_length=150)

    def __str__(self) -> str:
        return self.title