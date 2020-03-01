from django.shortcuts import render, redirect
from django import forms
from django.views.generic import View,TemplateView, ListView, DetailView, CreateView, UpdateView , DeleteView
from .forms import UserCreationForm, StudentProfileForm, FacultyProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import models
# Create your views here.

 ###########################################################################

class FacultyProfileList(ListView):
    context_object_name = 'facultys'
    model = models.FacultyProfile

############################################################################

class FacultyDetails(DetailView):
    context_object_name = 'faculty_details'

    model = models.FacultyProfile
    template_name = 'faculty_details.html'

#############################################################################

class FacultyAssign(CreateView):
    model = models.Teaches
    fields = ('faculty', 'subject', 'section')

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

@login_required
def student_portal(request,pk):
    if request.user.is_authenticated :
        user = request.user
        student = models.StudentProfile.objects.filter(user=user)[0]
        name = user.first_name.capitalize() +" "+ user.last_name.capitalize()
        year = student.year
        branch = student.branch.upper()
        semester = student.semester
        section = student.section.upper()
        subjects = models.Subject.objects.filter(branch=branch, year=year, semester=semester)
        user.subjects = subjects
        user.save()
        print(user.subjects)

        details = {
            'name' : name ,
            'reg_num' : user,
            'year' : year ,
            'branch' : branch ,
            'section' : section ,
            'semester' : semester,
            'subjects' : subjects
        }
    return render(request,'Feedback_System/student_portal.html',context = details)

##############################################################################

@login_required
def faculty_portal(request,pk):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/hod_portal')
        else:
            user = request.user
            faculty = models.FacultyProfile.objects.filter(user=user)[0]
            subjects = models.Teaches.objects.filter(faculty=faculty)
            user.subjects = subjects
            user.save()
            name = user.first_name.capitalize() + ' ' + user.last_name.capitalize()
            details = {
                'name' : name,
                'subjects' : subjects,
            }
    return render(request,'Feedback_System/faculty_portal.html',context=details)

##############################################################################

@login_required
def hod_portal(request):
    if request.user.is_authenticated:
        user = request.user
        faculty = models.FacultyProfile.objects.filter(user=user)
        subjects = models.Subject.objects.all()
        subj_list = [[s for s in subjects if s.year==i and s.semester==j] for i in range(1,5) for j in [1,2]]
        print(subj_list)
        name = user.first_name.capitalize() + ' ' + user.last_name.capitalize()
        details = {
            'name' : name,
            'years': range(1,5),
            'sections': ['A', 'B', 'c'],
            'subjects': subj_list,
        }
    return render(request,'Feedback_System/hod_portal.html',context = details)

##############################################################################

def about_us(request):
    return render(request,'Feedback_System/about_us.html',{})

#############################################################################
def student_register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        profile_form = StudentProfileForm(data=request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request,user)
            return redirect('/student_portal')
        else:
            return HttpResponse("Oops ! Some Error Occured !")
    else:
        form = UserCreationForm()
        profile_form = StudentProfileForm()
    return render(request, 'Feedback_System/student_register.html', {'form': form,
                                                  'profile_form': profile_form})
#
###############################################################################

def faculty_register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        profile_form = FacultyProfileForm(data=request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request,user)
            return redirect('/faculty_portal')
    else:
        form = UserCreationForm()
        profile_form = FacultyProfileForm()
    return render(request, 'Feedback_System/faculty_register.html', {'form': form,
                                                  'profile_form': profile_form})

# #############################################################################

def student_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(username=username)
        print(username, password)
        # if user.is_active:
        user = authenticate(username=username,password=password)
        print(user)
        if user:
            student = models.StudentProfile.objects.filter(user)
            if student.count()!=0:
                login(request,user)
                return HttpResponseRedirect('student_portal')
            else:
                return HttpResponseRedirect('Invalid Login !')
        else:
            return HttpResponse('Login failed !')
        # else:
        #     return HttpResponse(' Please Try Again !')
    return render(request,'Feedback_System/login.html',{})

# #############################################################################

def faculty_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            faculty = models.FacultyProfile.objects.filter(user)
            if faculty.count()!=0 or faculty.is_superuser:
                login(request,user)
                if faculty.is_superuser:
                    return HttpResponseRedirect('hod_portal')
                else:
                    return HttpResponseRedirect('faculty_portal')
            else:
                return HttpResponse('Login failed !')
        else:
            return HttpResponse(' Please Try Again !')
    return render(request,'Feedback_System/faculty_login.html',{})

##############################################################################

@login_required
def feedback(request,pk):
    user = request.user
    student = models.StudentProfile.objects.filter(user=user)[0]
    subject = models.Subject.objects.filter(id=pk)[0]
    faculty = models.Teaches.objects.filter(subject=subject, year=student.year,semester= student.semester)[0]
    print(student,subject,faculty)
    details = {
        'student' : student,
        'subject' : subject,
        'faculty' : faculty,
    }
    return render(request,'Feedback_System/feedback_form.html', context=details)

##############################################################################

def feedback_result(request):
    pass

##############################################################################

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

##############################################################################

def about_us(request):
    return render(request,'Feedback_System/about_us.html',{})
