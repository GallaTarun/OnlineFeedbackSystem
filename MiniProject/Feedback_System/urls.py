from django.conf.urls import include,url
from Feedback_System import views

app_name = 'project_app'

urlpatterns =[
    url(r'^home/',views.home,name='home'),
    url(r'^student_register/$',views.student_register,name='student_register'),
    url(r'^faculty_register/$',views.faculty_register,name='faculty_register'),
    url(r'^facultyprofile_list/$',views.FacultyProfileList.as_view(),name='facultyprofile_list'),
    url(r'^facultyprofile_list/(?P<pk>[-\w]+)/$',views.FacultyDetails.as_view(),name='faculty_details'),
    url(r'^user_logout/$',views.user_logout,name ='user_logout'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    # url(r'^about_us/$',views.about_us,name='about_us')
]
