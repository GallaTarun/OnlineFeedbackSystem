from django.contrib import admin
from .models import StudentProfile, FacultyProfile, Subject, Feedback, Teaches, Hod

# Register your models here.
admin.site.register(Subject)
admin.site.register(StudentProfile)
admin.site.register(FacultyProfile)
admin.site.register(Feedback)
admin.site.register(Teaches)
admin.site.register(Hod)
