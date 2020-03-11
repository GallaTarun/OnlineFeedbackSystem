from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile, FacultyProfile , Feedback
from django.core import validators

class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')
        help_texts = {
            'username': None,
            'email': None,
        }

        def save(self,commit=True):
            user = super().save(commit=false)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.password = self.cleaned_data['password']

            if commit:
                user.save()
            return user

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('branch','year','section','semester')

class FacultyProfileForm(forms.ModelForm):
    class Meta:
        model = FacultyProfile
        fields = ('age',)

class FeedbackForm(forms.ModelForm):
    ratings = ((5,'Very Good'),(4,'Good'),(3,'Average'),(2,'Below Average'),(1,'Poor'))
    res1 = forms.CharField(label='Clear and Audible voice',widget=forms.RadioSelect(choices=ratings))
    res2 = forms.CharField(label='Knowledge on Subject',widget=forms.RadioSelect(choices=ratings))
    res3 = forms.CharField(label='Student Interaction & Doubts Clarification',widget=forms.RadioSelect(choices=ratings))
    res4 = forms.CharField(label='Discipline and Control over class',widget=forms.RadioSelect(choices=ratings))
    res5 = forms.CharField(label='Passion & Enthusiasm to teach',widget=forms.RadioSelect(choices=ratings))
    res6 = forms.CharField(label='Punctual to class',widget=forms.RadioSelect(choices=ratings))
    res7 = forms.CharField(label='Covering Syllabus in time',widget=forms.RadioSelect(choices=ratings))
    res8 = forms.CharField(label='Sharing additional resources',widget=forms.RadioSelect(choices=ratings))
    class Meta:
        model = Feedback
        fields = ('res1','res2','res3','res4','res5','res6','res7','res8','sug')
