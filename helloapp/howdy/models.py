from django.db import models

# Create your models here.
from django.db import models


class Choice(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length=200, primary_key = True)
    password = models.CharField(max_length = 200)
    class Meta:
        db_table = "UserID"
    
