from django.db import models
from django.contrib.auth.models import User

class AllData(models.Model):
    name =  models.CharField(max_length=100)
    email =  models.CharField(max_length=100)
    caption = models.TextField()
    op1 = models.CharField(max_length=100)
    op2 = models.CharField(max_length=100)
    op3 = models.CharField(max_length=100)
    op4 = models.CharField(max_length=100)

