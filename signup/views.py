from django.shortcuts import render, HttpResponse, redirect
from signup.models import ProfileImage
from .forms import ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control



def index(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        data = request.POST
        print(data)
        if form.is_valid():
            form.save()
            messages.success(request, "your account has been successfully created")
    else:
        form =  ProfileForm()
    return render(request,'c_signup.html',{'form':form})
"""
# Create your views here.
def index(request):
    returnvariable = 0
    if request.method == 'POST':        
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = request.POST
            print(data)
            name = data.get('name')
            password = data.get('password')
            repeatpassword =  data.get('repeat_password')
            profile = ProfileImage.objects.filter(name=name)
            if profile:
                user_exist_message = "Sorry, User name is taken!"
                returnvariable  = render(request, 'signup.html', {'form':form, 'user_exist_message':user_exist_message})
            elif password != repeatpassword:
                password_mismatch_message= "Sorry, Password mismatch!" 
                returnvariable = render(request, 'signup.html',{'form':form,'password_mismatch_message':password_mismatch_message})
            else:    
                print("Record has been saved successfully!")
                form.save()              
                returnvariable = redirect('success')
        return returnvariable
    else:
        form = ProfileForm()
        return render(request, 'signup.html',{'form':form})
        """
    
def showform(request):
    form = ProfileForm()
    return render(request,'signup.html',{'form':form})

def showimage(request):
    # ProfileImage.objects.all().delete()
    print("show image view")

    return HttpResponse("database deleted!")
  
def success(request):
    user_success_message = "User has been added successfully!"
    return render(request,'success.html',{'user_success_message':user_success_message})

def dbtest(request):
    a = ProfileImage.objects.all()
    b = ProfileImage.objects.get(id=36)
    c = ProfileImage.objects.get(pk=36)  #this is because 1-35 records are deleted
    print("this is b:",b.email)
    print("this is c:",c.email)
    # a = "hello"
    for x in a:
        print(x.name)
        print(x.email)
    print(a)
    return HttpResponse("Database test")

def testreturn(request):
    var = 0
    a = 2
    if a == 0:
        var = render(request,'success.html')
    else:
        form = ProfileForm()
        var = render(request,"signup.html",{'form':form})
    return HttpResponse(var)
