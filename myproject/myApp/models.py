# first we need to register our model, then only these tables will get stored in some db
from django.db import models

# Create your models here.

#following is the events table with it's fields
class Events(models.Model):
    # let's first declare the columns of our events table
    # id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    from_date = models.DateField()
    to_date = models.DateField()
    host_email = models.EmailField(max_length=200)
    host_pw = models.CharField(max_length=10)
    deadline_date = models.DateField()

    def __str__(self):
        return  self.name
