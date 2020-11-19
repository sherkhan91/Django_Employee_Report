from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Leaves(models.Model):
    username = models.CharField(max_length=100)
    reason = models.CharField(max_length=1000)
    date = models.DateField(max_length=500)
    time = models.TimeField()

class Employee(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='employee')
    empuser = models.CharField(max_length=100, editable=False)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    profileimage = models.ImageField(upload_to='images/', default='defaultimage', blank=True, null=True)

    def __str__(self):
        return self.empuser

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Employee.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender,instance, **kwargs):
#     instance.employee.save()

class UserReportModel(models.Model):
    user =  models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    feedback = models.CharField(max_length=500)
    date = models.DateField(max_length=500)
    time = models.TimeField()

    def __str__(self):
        return self.user

class profileimage(models.Model):
    name = models.CharField(max_length=50,default='defaultname')
    profile_image = models.ImageField(upload_to='images/', default='defaultimage')
    # password =  models.CharField(max_length=20, default='defaultpassword')
    # repeat_password =  models.CharField(max_length=20, default='defaultrepeatpassword')
    # email = models.CharField(max_length=50, default='default@email.com')
    # class Meta:
        # db_table = "profileimage"
        # db_table = "login_profileimage"

    def __str__(self):
        return self.name


