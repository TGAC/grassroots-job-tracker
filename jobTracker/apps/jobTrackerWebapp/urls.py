from django.conf.urls import url, include
from django.contrib import admin

import apps.jobTrackerWebapp.views as views

urlpatterns = [
    url(r'^$', views.rest_index, name='rest_index'),
    # url(r'^insert_person', views.mongo_insert, name="insert"),
    url(r'^view_all_jobs', views.mongo_view_all_jobs, name="view_all_jobs"),
    # url(r'^view_all', views.mongo_view, name="view"),
    url(r'^insert_job', views.mongo_insert_job, name="insert_job"),
    url(r'^get_job', views.mongo_get_job, name="get_job"),
    url(r'^update_job', views.mongo_update_job, name="update_job")
]
