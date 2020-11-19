from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserReportModel
from django.forms import ModelForm

from django import forms
from .models import Employee
from .models import profileimage,Leaves


class leaveform(ModelForm):
    class Meta:
        model = Leaves
        fields = '__all__'

# class ProfileImage(ModelForm):
class profileimageform(ModelForm):
    # name = forms.CharField(max_length=100)
    profile_image = forms.ImageField()
    
    class Meta:
        model = profileimage
        fields = '__all__'


class UserReport(ModelForm):
    class Meta:
        model = UserReportModel
        fields = '__all__' 

 
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'



class ProfileForm(UserCreationForm):
    # # imagefile =  forms.FileField()
    # designation = forms.CharField(max_length=200, required=False)
    # department = forms.CharField(max_length=100, required=True)
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','date_joined')

