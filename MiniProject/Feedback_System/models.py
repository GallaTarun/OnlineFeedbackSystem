from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import RegexValidator


class Subject(models.Model):
    name = models.CharField(max_length=250, blank=False)
    branch = models.CharField(max_length=5)
    year = models.IntegerField(default=1)
    semester = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    branches = (('CSE','CSE'),('ECE','ECE'),('IT','IT'),('MECH','MECH'),('EEE','EEE'),('CHEM','CHEM'))
    years = ((1,1),(2,2),(3,3),(4,4))
    semesters = ((1,1),(2,2))
    sections= (('A','A'),('B','B'),('C','C'))
    gender = (('M','Male'),('F','Female'))
    gender = models.CharField(choices=gender,default='M',max_length=1)
    branch = models.CharField(choices=branches,default='CSE',max_length=10)
    year = models.PositiveSmallIntegerField(choices=years,default=1)
    subject = models.ManyToManyField(Subject, related_name="subject_students")
    section = models.CharField(choices=sections,max_length=1)
    semester = models.IntegerField(choices=semesters,default=1)

    def __str__(self):
         return self.user.username


class FacultyProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    subject = models.ManyToManyField(Subject, related_name="subject_teachers")

    def __str__(self):
        return self.user.username


class Hod(models.Model):
    branches = (('CSE','CSE'),('ECE','ECE'),('IT','IT'),('MECH','MECH'),('EEE','EEE'),('CHEM','CHEM'))
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    department = models.CharField(choices=branches,default='CSE',max_length=10)


    def __str__(self):
        return self.user.username


class Feedback(models.Model):
    student = models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    teacher = models.ForeignKey(FacultyProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    submitted = False

    res1 = models.CharField(max_length=10)
    res2 = models.CharField(max_length=10)
    res3 = models.CharField(max_length=10)
    res4 = models.CharField(max_length=10)
    res5 = models.CharField(max_length=10)
    res6 = models.CharField(max_length=10)
    res7 = models.CharField(max_length=10)
    res8 = models.CharField(max_length=10)
    sug = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.student.user.username + "--" + self.subject.name

class Teaches(models.Model):
    faculty = models.ForeignKey(FacultyProfile,on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete = models.CASCADE)
    years = (('1','1'),('2','2'),('3','3'),('4','4'))
    sections = (('A','A'),('B','B'),('C','C'))
    semesters = ((1,1),(2,2))
    year = models.CharField(max_length=1,choices=years,default='1')
    semester = models.IntegerField(choices=semesters,default=1)
    section = models.CharField(max_length=1,choices=sections,default='A')


    def get_absolute_url(self):
        return reverse('project_app:faculty_portal')

    def __str__(self):
        return self.faculty.user.username + " " + self.subject.name
