from django.contrib import admin
from django.conf.urls import url,include
from Feedback_System import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    url(r'^',include('Feedback_System.urls',namespace='project_app')),
]
