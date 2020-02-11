from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class StudentProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    branch = models.CharField(max_length=10)
    year = models.PositiveSmallIntegerField()
    section = models.CharField(max_length=1)

    def __str__(self):
         return self.user.username


class FacultyProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    age = models.PositiveIntegerField()
    # subjects = models.OnetoManyField(Subject,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username




# class Subject(models.Model):
#     name = models.CharField(max_length=250, blank=False)
#     year = models.IntegerField(default=1)
#     semester = models.IntegerField(default=1)
#
#     def __str__(self):
#         return self.name



# class Feedback(models.Model):
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     teacher = models.ForeignKey(Faculty, on_delete=models.CASCADE)
#     res1 = models.IntegerField(default=1)
#     res2 = models.IntegerField(default=1)
#     res3 = models.IntegerField(default=1)
#     res4 = models.IntegerField(default=1)
#     res5 = models.IntegerField(default=1)
#     sug = models.CharField(max_length=500, blank=True, null=True)
#
#     def __str__(self):
#         return self.student.user.username + " - " + self.subject.name
