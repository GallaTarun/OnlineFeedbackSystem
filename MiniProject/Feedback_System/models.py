from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



class Subject(models.Model):
    name = models.CharField(max_length=250, blank=False)
    branch = models.CharField(max_length=5)
    year = models.IntegerField(default=1)
    semester = models.IntegerField(default=1)

    def __str__(self):
        return self.name +"--"+ self.year +"--"+ self.semester


class StudentProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    branch = models.CharField(max_length=10)
    year = models.PositiveSmallIntegerField()
    subject = models.ManyToManyField(Subject, related_name="subject_students")
    section = models.CharField(max_length=1)
    semester = models.CharField(max_length=1,default=1)

    def __str__(self):
         return self.user.username


class FacultyProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    subject = models.ManyToManyField(Subject, related_name="subject_teachers")

    def __str__(self):
        return self.user.username


class Feedback(models.Model):
    student = models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    teacher = models.ForeignKey(FacultyProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    res1 = models.IntegerField(default=1)
    res2 = models.IntegerField(default=1)
    res3 = models.IntegerField(default=1)
    res4 = models.IntegerField(default=1)
    res5 = models.IntegerField(default=1)
    sug = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.student.user.username + "--" + self.subject.name
