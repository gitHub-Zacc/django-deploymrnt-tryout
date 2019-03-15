from django.shortcuts import render
from .forms import UserInfo, UserProfileInfo

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
# from django.http import HttpResponse
# from AppTwo.models import User
# from .forms import NewUser
# Create your views here.
def home(request):
    content = {}
    return render(request, "AppTwo/home.html", context=content)

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def users(request):

    registered = False
    if request.method == "POST":
        user_form = UserInfo(data=request.POST)
        profile_form = UserProfileInfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            reqistered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserInfo()
        profile_form = UserProfileInfo()
    signUp_content = {'user_form':user_form, 'profile_form':profile_form, 'registered':registered}
    return render(request,'AppTwo/users.html',context=signUp_content)

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("<h1>ACCOUNT NOT ACTIVE</h1>")
        else:
            print("login fail happened")
            print("username: {} and password: {}".format(username,password))
            return HttpResponse("Make sure your username and password are spelled corectly or are registered with you sign up")
    return render(request,'AppTwo/login.html',{})
