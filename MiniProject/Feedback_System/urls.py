from django.conf.urls import include,url
from Feedback_System import views
from django.contrib.auth.views import LoginView
app_name = 'project_app'

urlpatterns =[
    url(r'^home/',views.home,name='home'),
    url(r'^student_register/$',views.student_register,name='student_register'),
    url(r'^faculty_register/$',views.faculty_register,name='faculty_register'),
    url(r'^facultyprofile_list/$',views.FacultyProfileList.as_view(),name='facultyprofile_list'),
    url(r'^facultyprofile_list/(?P<pk>[-\w]+)/$',views.FacultyDetails.as_view(),name='faculty_details'),
    url(r'^student_login/$',views.student_login,name ='student_login'),
    url(r'^faculty_login/$',views.faculty_login,name ='faculty_login'),
    url(r'^user_logout/$',views.user_logout,name='user_logout'),
    url(r'^student_portal/$',views.student_portal,name='student_portal'),
    url(r'^faculty_portal/$',views.faculty_portal,name='faculty_portal'),
    url(r'^hod_portal/$',views.hod_portal,name="hod_portal"),
    url(r'^assign_faculty/$',views.FacultyAssign.as_view(),name='assign_faculty'),
    url(r'^about_us/$',views.about_us,name='about_us'),
    url(r'^student_portal/feedback/(?P<pk>[-\w]+)/$',views.feedback,name='feedback_form'),
    url(r'^feedback_result/(?P<pk>[-\w]+)/$',views.feedback_result,name='feedback_result'),
]
