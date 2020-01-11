"""ecommhome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# for ability to server static contect - not for prod envs
from django.conf import settings
from django.conf.urls.static import static

# import the custom view 
from .myviews import myhome, mycontacts, myaboutus, mylogin, myregister

from students.views import StudentListView, Student_ListView, StudentDetailView, Student_DetailView


urlpatterns = [
    url(r'^$', myhome),
    url(r'^contacts/$', mycontacts),
    url(r'^aboutus/$', myaboutus),
    url(r'^login/', mylogin),
    url(r'^register/', myregister),
    url(r'^admin/', admin.site.urls),

    # urls for list view
    url(r'^students/$', StudentListView.as_view()),
    url(r'^students-fv/$', Student_ListView),

    #urls for detail view ( use Regex so that for detailview we can pass id/primarykey)
    url(r'^students/(?P<pk>\d+)/$', StudentDetailView.as_view()),
    url(r'^students-fv/(?P<pk>\d+)/$', Student_DetailView),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)