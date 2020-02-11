from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile, FacultyProfile
from django.core import validators

class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')
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
        fields = ('branch','year','section')

class FacultyProfileForm(forms.ModelForm):
    class Meta:
        model = FacultyProfile
        fields = ('age',)
