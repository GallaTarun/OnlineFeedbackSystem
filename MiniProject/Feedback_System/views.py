from django.shortcuts import render, redirect
from django import forms
from django.views.generic import View,TemplateView, ListView, DetailView
from .forms import UserCreationForm, StudentProfileForm, FacultyProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import models
# Create your views here.

class FacultyProfileList(ListView):
    context_object_name = 'facultys'
    model = models.FacultyProfile

############################################################################

class FacultyDetails(DetailView):
    context_object_name = 'faculty_details'

    model = models.FacultyProfile
    template_name = 'faculty_details.html'


#############################################################################
def home(request):
    intro = {
            'one' : "Welcome to ONLINE FEEDBACK SYSTEM!",
            'two' : "Give the feedback to the faculty teaching you ",
            'three' : "View neccessary details here .. "
    }
    return render(request,'Feedback_System/home_page.html',context = intro)

#############################################################################
def thankyou(request):
    dic = {
        'wish' : "Thanks For Registering ..",
        'redirect' : "Please redirect to Login Page !!",
    }
    return render(request,'Feedback_System/thankyou.html',context = dic)
#############################################################################

def about_us(request):
    return render(request,'Feedback_System/about_us.html',{})

#############################################################################
def student_register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        profile_form = StudentProfileForm(data=request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return render(request, 'Feedback_System/thankyou.html',{'wish': 'Thanks For Registering' , 'redirect': 'Please redirect to Login Page !!'})
    else:
        form = UserCreationForm()
        profile_form = StudentProfileForm()
    return render(request, 'Feedback_System/student_register.html', {'form': form,
                                                  'profile_form': profile_form})
#
# # #############################################################################
def faculty_register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        profile_form = FacultyProfileForm(data=request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return render(request, 'Feedback_System/thankyou.html',{'wish': 'Thanks For Registering' , 'redirect': 'Please redirect to Login Page !!'})
    else:
        form = UserCreationForm()
        profile_form = FacultyProfileForm()
    return render(request, 'Feedback_System/faculty_register.html', {'form': form,
                                                  'profile_form': profile_form})

# #############################################################################
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email,password=password)

        if user:
            if user.is_active is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                HttpResponse("Account Not Active !")
        else:
            print("Someone tried to login and failed !")
            print("Email ID : {} and Password :{}".format(email,password))
            return HttpResponse("Invalid Credentials")
    else:
        return render(request,'Feedback_System/login.html',{})

# #############################################################################
#
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
