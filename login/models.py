from django.db import models

# Create your models here.

class UserReportModel(models.Model):
    user =  models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    feedback = models.CharField(max_length=500)
    date = models.DateField(max_length=500)
    time = models.TimeField()

    def __str__(self):
        return self.user


