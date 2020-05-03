from django.shortcuts import render, redirect
from django import forms
from django.views.generic import View,TemplateView, ListView, DetailView, CreateView, UpdateView , DeleteView
from .forms import UserCreationForm, StudentProfileForm, FacultyProfileForm, FeedbackForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import models


 ###########################################################################

class FacultyProfileList(ListView):
    context_object_name = 'facultys'
    model = models.FacultyProfile

############################################################################

class FacultyDetails(DetailView):
    context_object_name = 'facultydetails'

    model = models.FacultyProfile
    template_name = 'Feedback_System/faculty_details.html'

#############################################################################

class FacultyAssign(CreateView):
    model = models.Teaches
    fields = ('faculty', 'subject', 'year' , 'section', 'semester')

#############################################################################

def is_hod(request,user):
    hod = models.Hod.objects.all()
    if user in hod:
        return True
    else:
        return False

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
def student_portal(request):
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
def faculty_portal(request):
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
        faculty = models.Teaches.objects.all()
        # subj_list = [[s for s in subjects if s.year==i and s.semester==j ] for i in range(1,5) for j in [1,2]]
        name = user.first_name.capitalize() + ' ' + user.last_name.capitalize()

        details = {
            'name' : name,
            'years': range(1,5),
            'sections': ['A', 'B', 'c'],
            # 'subjects': subj_list,
            'faculty': faculty,
        }
    else:
        return HttpResponse("You dont have permissions to access this page !")
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

            year = request.POST.get('year')
            branch = request.POST.get('branch')
            semester = request.POST.get('semester')
            section = request.POST.get('section')
            print(year,branch,semester,section)

            subjects = list(models.Subject.objects.filter(branch=branch,year=year,semester=semester))
            print(subjects)

            for subject in subjects:
                faculty = models.Teaches.objects.filter(subject=subject,section=section)
                print(faculty)
                # fd = models.Feedback(student=request.user,subject=subject,teacher=faculty)
                # fd.save(commit=False)

            return redirect('/student_portal')
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
        user = get_object_or_404(User,username=username,password=password)
        user.backend = None
        if user:
            login(request,user)
        else:
            return HttpResponse('Login failed !')
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
    if request.user.is_authenticated:
        user = request.user
        student = models.StudentProfile.objects.filter(user=user)[0]
        subject = models.Subject.objects.filter(id=pk)[0]
        faculty = models.Teaches.objects.filter(subject=subject, year=student.year,semester= student.semester)[0]
        print(student,subject,faculty.faculty)
        # feedback_obj = models.Feedback.objects.filter(subject=subject,teacher=faculty.faculty,student=student)[0]
        # print(feedback_obj)
        form = FeedbackForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                feedback = form.save(commit=False)
            else:
                form = FeedbackForm()

        #     r1= request.POST.get('q1')
        #     r2 = request.POST.get('q2')
        #     r3 = request.POST.get('q3')
        #     r4 = request.POST.get('q4')
        #     r5 = request.POST.get('q5')
        #     r6 = request.POST.get('q6')
        #     r7 = request.POST.get('q7')
        #     r8 = request.POST.get('q8')
        #     sug = request.POST.get('suggestion')
        #

    details = {
        'student' : student,
        'subject' : subject,
        'faculty' : faculty,
        'form' : form,
    }
    return render(request,'Feedback_System/feedback_form.html', context=details)

##############################################################################

@login_required
def feedback_result(request,pk):
    feedback = models.Teaches.objects.filter(id=pk)[0]
    print(feedback)
    details = {
        'feedback' : feedback,
    }
    return render(request,'Feedback_System/feedback_result.html',context=details)

##############################################################################

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

##############################################################################

def about_us(request):
    return render(request,'Feedback_System/about_us.html',{})
