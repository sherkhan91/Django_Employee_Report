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

class UserReport(ModelForm):
    class Meta:
        model = UserReportModel
        fields = '__all__' 