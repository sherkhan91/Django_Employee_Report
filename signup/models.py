from django.db import models

# Create your models here.
class ProfileImage(models.Model):
    name = models.CharField(max_length=50,default='defaultname')
    profile_image = models.ImageField(upload_to='images/', default='defaultimage')
    password =  models.CharField(max_length=20, default='defaultpassword')
    repeat_password =  models.CharField(max_length=20, default='defaultrepeatpassword')
    email = models.CharField(max_length=50, default='default@email.com')




   
