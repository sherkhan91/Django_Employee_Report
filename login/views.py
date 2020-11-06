from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from .models import profileimage
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .forms import UserReport
from .models import UserReportModel
from django.contrib.auth.models import User 
from .models import Employee
import json
from datetime import datetime
from .forms import ProfileForm
import time
from django.core.files.storage import FileSystemStorage
from .forms import profileimageform
from .forms import EmployeeForm
# Create your views here.



def profileimg(request):
   
    if request.method == "POST":
        myprofileform = profileimageform(request.POST, request.FILES)
        # print("data is:", request.POST)
        if myprofileform.is_valid():
            # print("form is valid")
            # print(form.POST)
            # mprofile = myprofileform.cleaned_data["name"]
            # mprofile = myprofileform.cleaned_data["profile_image"]
            myprofileform.save()
        else:
            # print("invalid.........")
            pass
    form = profileimageform()
    return render(request, 'profileimage.html',{'form':form})



def index(request):
    print("this is where im looking for something")
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
        print("this is date joined:",request.user.date_joined)
        date_joined = request.user.date_joined
        # date_joined =  datetime.strptime(str(request.user.date_joined),'%Y-%m-%d')
        designation= "Python Developer" 
        join_date = str(date_joined.date())
        # print(date_joined.date())
        return render(request,'user_profile.html',{'name':request.user.username,'email':request.user.email,'join_date':join_date})
    # return HttpResponse("hello")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='index')
def user_home(request):
    
    print("hello")
    if not request.user.is_authenticated:
        return redirect('index')
    elif request.user.is_superuser:
        return redirect('admin_home')
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


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='index')
def admin_home(request):
    # return redirect('logout')
    if not request.user.is_authenticated:
        return redirect('index')
    elif request.user.is_superuser == True:
        # print("yes i'm admin ")
        stime = '14:00:22:123456'
        etime = '18:00:22:123456'
        # from datetime import datetime
        # start_time = start_date.strptime(time_string, "HH:MM[:ss[.uuuuuu]]")
        # end_time = end_date.strptime(time_string, "HH:MM[:ss[.uuuuuu]]")
        yesterday = '2020-10-22'
        choosedate = '2020-10-26'
        todaysDate      = datetime.today().strftime('%Y-%m-%d')
        # print('todays date:',todaysDate)  # get todays date
        entry =  UserReportModel.objects.filter(date=choosedate).filter(time__range=['09:00[:00[.232323]]','23:10[:00[.232323]]'])
        # entry =  UserReportModel.objects.filter(date=yesterday).filter(time__range=['14:00[:00[.232323]]','23:10[:00[.232323]]'])
        # entry =  UserReportModel.objects.filter(date=datetime.date(datetime.now())).filter(time__range=['14:00[:00[.232323]]','23:10[:00[.232323]]'])

        users = []
        pnames = []
        pdescriptions = []
        ptimes = []
        # print("done with it")
        # from django.utils import simplejson
        for i in range(len(entry)):
            users.append(entry[i].user)
            pnames.append(entry[i].name)
            ptimes.append(str(entry[i].time))
            pdescriptions.append(entry[i].description)
            # print(i,entry[i].user, entry[i].name, entry[i].description, entry[i].date, entry[i].time)
    
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
        userdata = {}
        ids = []
        empids = []
        users = User.objects.values('id','username','date_joined')
        for x in users:
            ids.append(x['id'])
 
        allemployees = Employee.objects.filter(empuser__in=ids).values('department','designation','profileimage','empuser')
        for y in allemployees:
            empids.append(y['empuser'])

        allusers = User.objects.values('id','username','date_joined').filter(id__in=empids)

        for i in range(len(allusers)):
            allusers[i]['department'] = allemployees[i]['department']
            allusers[i]['designation'] = allemployees[i]['designation']
            allusers[i]['profileimage'] =allemployees[i]['profileimage']
            
        return render(request,'admin_users.html',{'allusers':allusers})
    else:
        return redirect('logout')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='index')
def admin_addemployee(request):
    profile =  ProfileForm()
    employee = EmployeeForm()
    if request.method == "POST":
        myprofile = ProfileForm(request.POST)
        myemployee = EmployeeForm(request.POST, request.FILES)
        print(request.POST)
        if myprofile.is_valid() and myemployee.is_valid():
            myprofile.save()
            userid =  User.objects.get(username=myprofile['username'].value()).pk
            img = myemployee['profileimage'].value()
            p1 =  Employee(department=myemployee['department'].value(),designation=myemployee['designation'].value(),profileimage=img, empuser=userid)
            p1.save()
            # myemployee.profileimage = myemployee['profileimage']
            # myemployee.save()
        else:
            pass
        
    return render(request,'addemployee.html',{'profileform':profile,'employeeform':employee})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='index')
def admin_lazyusers(request):
    print("yes im here...")
    if not request.user.is_authenticated:
        return redirect('index')
    elif request.user.is_superuser == True:
        todaysDate = datetime.today().strftime('%Y-%m-%d')
        startTime = '14:00[:00[.001122]]'
        endTime = '23:00[:00[.002233]]'
        choosenDate = '2020-10-26'
        names = []
        dummyDepartment = []
        times = []
        entry =  UserReportModel.objects.values_list('user','date','time').filter(date=choosenDate).filter(time__range=['09:00[:00[.232323]]','23:10[:00[.232323]]'])
        # entry =  UserReportModel.objects.values_list('feedback',flat=True)
        # entry = UserReportModel.objects.filter(date=choosenDate).filter(time__range=[startTime,endTime])
        
        print("length of ------- entry:", len(entry))
        for i in range(len(entry)):
            print(entry[i][0],entry[i][1], entry[i][2])
            names.append(str(entry[i][0]))
            dummyDepartment.append("Dummy Department")
            times.append(str(entry[i][2]))
        lazyuser = [names, dummyDepartment, times] 
        lazyusers = json.dumps(lazyuser)
        return render(request,'admin_lazyusers.html',{'lazyusers':lazyusers})
    else:
        return redirect('logout')

def admin_addemployeereal(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        data = request.POST
        print(data)

        if form.is_valid():
            print("yes form is valuid")
            form.save()
            messages.success(request, "employee account has been successfully created")
        else:
            print("Sorry form is invalid")
    else:
        form =  ProfileForm()
    return render(request,'addemployee.html',{'form':form})

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