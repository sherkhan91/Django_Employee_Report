from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from signup.models import ProfileImage
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from  signup.forms import ProfileForm 
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .forms import UserReport
from .models import UserReportModel
import json

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                # print(form)
                name = form.cleaned_data['username']
                passw = form.cleaned_data['password']
                user = authenticate(username=name, password=passw)
                if user is not None and user.is_superuser:
                    login(request, user)
                    # returnval =  HttpResponseRedirect("user_profile")
                    return render(request,'admin_home.html',{'name':name})
                else:
                    login(request,user)
                    return render(request,'user_home.html',{'name':name})
                
        else:
            form = AuthenticationForm()
        return render(request, 'c_login.html', {'form':form})
    else:
        return HttpResponseRedirect('user_home')


"""
def index(request):
    returnpath = 0
    message = ""
    if request.method == 'POST':
        data = request.POST
        print(data)
        user = data.get('inputname')
        userpassword = data.get('password')
        profile =  0
    
        
        profile = ProfileImage.objects.filter(name=user).exists()

        if(profile):
            print("user exists")
            name = ProfileImage.objects.get(name=user).name
            passw =  ProfileImage.objects.get(name=user).password
            imageurl =  ProfileImage.objects.get(name=user).profile_image
            if userpassword ==  passw:
                print("logged in")
                print("voew your image", imageurl)
                a = name
                if name == 'admin':
                    returnpath =  render(request,'admin.html')
                else:
                    returnpath = render(request, 'user_home.html',{'a':a,'imageurl':imageurl})
                # returnpath = render(request,'login.html',{'message':message})   
                # returnpath = render(request,'profile.html',{'a':a,'imageurl':imageurl})
            else:
                # print("Sorry wrong password")
                message = "Sorry wrong password"
                returnpath = render(request,'login.html',{'message':message})   
        else:
            print("sorry user does not exist")
            message = "Sorry user does not exist"
            returnpath =  render(request,'login.html',{'message':message})
        return returnpath
    else:
        returnpath = render(request,'login.html')
        return returnpath
 """

def profile(request):
    # print(hello)
    return HttpResponse("this is response")

def logout_request(request):
    logout(request)
    return HttpResponseRedirect('/login')
    # return HttpResponse("Logout page")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='index')
def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        users = ProfileForm(instance=request.user)
        return render(request,'user_profile.html',{'name':request.user.username,'email':request.user.email})
    # return HttpResponse("hello")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='index')
def user_home(request):
    print("hello")
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            data =  request.POST
            print(data)
            userReportForm = UserReport(request.POST)
            if userReportForm.is_valid():
                print("yes data is valid")
                userReportForm.save()
            else:
                print("no its not")
        
        users =  ProfileForm(instance=request.user)
        userReportForm = UserReport()

        return render(request, 'user_home.html',{'name': request.user.username, 'formm':userReportForm})
    

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='index')
def user_leave(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request,'user_leave.html')
    


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='index')
def user_editprofile(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request,'user_editprofile.html')      

from datetime import datetime
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='index')
def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('index')
    elif request.user.is_superuser == True:
        print("yes i'm admin ")
        stime = '14:00:22:123456'
        etime = '18:00:22:123456'
        # from datetime import datetime
        # start_time = start_date.strptime(time_string, "HH:MM[:ss[.uuuuuu]]")
        # end_time = end_date.strptime(time_string, "HH:MM[:ss[.uuuuuu]]")
        yesterday = '2020-10-22'
        choosedate = '2020-10-26'
        todaysDate      = datetime.today().strftime('%Y-%m-%d')
        print('todays date:',todaysDate)  # get todays date
        entry =  UserReportModel.objects.filter(date=choosedate).filter(time__range=['14:00[:00[.232323]]','23:10[:00[.232323]]'])
        # entry =  UserReportModel.objects.filter(date=yesterday).filter(time__range=['14:00[:00[.232323]]','23:10[:00[.232323]]'])
        # entry =  UserReportModel.objects.filter(date=datetime.date(datetime.now())).filter(time__range=['14:00[:00[.232323]]','23:10[:00[.232323]]'])

        users = []
        pnames = []
        pdescriptions = []
        ptimes = []
        print("done with it")
        # from django.utils import simplejson
        for i in range(len(entry)):
            users.append(entry[i].user)
            pnames.append(entry[i].name)
            ptimes.append(str(entry[i].time))
            pdescriptions.append(entry[i].description)
            print(i,entry[i].user, entry[i].name, entry[i].description, entry[i].date, entry[i].time)
    
        detaillist = json.dumps([users,pnames,ptimes,pdescriptions])
        context = {'users':users,'pnames':pnames,'pdescriptions':pdescriptions,'ptimes':ptimes}
        return render(request,'admin_home.html',{'detaillist':detaillist})
    else:
        return redirect('logout')
    

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='index')    
def admin_feedback(request):
    if not request.user.is_authenticated:
        return redirect('index')
    elif request.user.is_superuser == True:
        feedbacks = []
        users = []
        entry =  UserReportModel.objects.values_list('feedback',flat=True)
        entry2 = UserReportModel.objects.values_list('user', flat=True)
        for i in range(len(entry)):
            # print(entry[i])
            users.append(str(entry2[i]))
            feedbacks.append(str(entry[i]))

        feedback = json.dumps([users,feedbacks])

        print(feedback)
        # detaillist = json.dumps([users,pnames,ptimes,pdescriptions])
        # context = {'users':users,'pnames':pnames,'pdescriptions':pdescriptions,'ptimes':ptimes}
        # return render(request,'admin_home.html',{'detaillist':detaillist})

        return render(request,'admin_feedback.html',{'feedback':feedback})
    else:
        return redirect('logout')
    

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='index')
def admin_leaves(request):
    if not request.user.is_authenticated:
        return redirect('index')
    elif request.user.is_superuser == True:
        return render(request,'admin_leaves.html')
    else:
        return redirect('logout')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='index')    
def admin_users(request):
    if not request.user.is_authenticated:
        return redirect('index')
    elif request.user.is_superuser==True:
        return render(request,'admin_users.html')
    else:
        return redirect('logout')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='index')
def admin_lazyusers(request):
    if not request.user.is_authenticated:
        return redirect('index')
    elif request.user.is_superuser == True:
        return render(request,'admin_lazyusers.html')
    else:
        return redirect('logout')


def checkdatabase(request):
    entry = UserReportModel.objects.get(pk=1)
    print(entry)
    return HttpResponse("this is a check")
"""
def index(request):
    form =  AuthenticationForm()
    return render(request, 'loginm.html', {'form':form})
"""




"""
def index(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                print(form)
                name = form.cleaned_data['username']
                passw = form.cleaned_data['password']
                user = authenticate(username=name, password=passw)
                if user is not None:
                    login(request, user)
                    # returnval =  HttpResponseRedirect("user_profile")
                    return HttpResponseRedirect('user_home')
        else:
            form = AuthenticationForm()
        return render(request, 'loginm.html', {'form':form})
    else:
        return HttpResponseRedirect('user_home')
"""