"""jobTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include, handler404, handler500
from django.contrib import admin
import apps.jobTrackerWebapp.urls as rest_urls
import apps.jobTrackerWebapp.views as views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^view_jobs', views.mongo_view_all_jobs, name="view_all_jobs"),
    url(r'^view_job/(?P<job_id>[A-z0-9-]+)$', views.mongo_view_job, name="view_job"),
    url(r'^admin/', admin.site.urls),
    url(r'^rest/', include(rest_urls), name='rest_urls'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATICFILES_DIRS})
]

handler404 = views.error404_handler
handler500 = views.error500_handler