from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterationForm, UserProfileForm

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse("welcome you. You hava been authenticated successfully")
            else:
                return HttpResponse("Invalid login")
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})



def register(request):
    if request.method == "POST":
        user_form = RegisterationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()

            return HttpResponse("successfully")
        else:
            return HttpResponse("sorry, your can not register.")
    else:
        user_form = RegisterationForm()
        userprofile_form = UserProfileForm()
        return render(request, "account/register.html", {"form": user_form, "profile":userprofile_form})


