# # forms.py 
# from django.forms import ModelForm, TextInput
# from .models import *
# from django import forms
  
# class ProfileForm(ModelForm): 
  
#     class Meta: 
#         model = ProfileImage
#         fields = ['name', 'profile_image','password','repeat_password','email']
#         widgets = {
#             'name': TextInput(attrs={'cols':10, 'rows':3}),
#             'password': forms.PasswordInput(),
#             'repeat_password': forms.PasswordInput(),

#         }
#     def clean_username(self):
#         username = self.cleaned_data['name']
#         try:
#             user = ProfileImage.objects.get(name=username)
#         except user.DoesNotExist:
#             return username
#         raise forms.ValidationError(u'Username "%s" is already is in use '%username)
    
 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserReportModel
from django.forms import ModelForm

from django import forms
from .models import Employee


# class ProfileImage(ModelForm):



class UserReport(ModelForm):
    class Meta:
        model = UserReportModel
        fields = '__all__' 

 


class ProfileForm(UserCreationForm):
    image =  forms.ImageField()
    designation = forms.CharField(max_length=200, required=True)
    department = forms.CharField(max_length=100, required=True)
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','date_joined','image','department','designation')
    
    # def save(self,commit=True):
    #     user= super(UserCreationForm,self).save(commit=False)
    #     user.designation = self.cleaned_data['designation']
    #     user.department = self.cleaned_data['department']
    #     if commit:
    #         user.save()
    #     return user





# # forms.py 
# from django.forms import ModelForm, TextInput
# from .models import *
# from django import forms
  
# class ProfileForm(ModelForm): 
  
#     class Meta: 
#         model = ProfileImage
#         fields = ['name', 'profile_image','password','repeat_password','email']
#         widgets = {
#             'name': TextInput(attrs={'cols':10, 'rows':3}),
#             'password': forms.PasswordInput(),
#             'repeat_password': forms.PasswordInput(),

#         }
#     def clean_username(self):
#         username = self.cleaned_data['name']
#         try:
#             user = ProfileImage.objects.get(name=username)
#         except user.DoesNotExist:
#             return username
#         raise forms.ValidationError(u'Username "%s" is already is in use '%username)
    
