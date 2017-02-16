from django.conf.urls import url, include
from django.contrib import admin

import apps.jobTrackerWebapp.views as views

urlpatterns = [
    url(r'^$', views.rest_index, name='rest_index'),
    url(r'^insert_person', views.mongo_insert, name="insert"),
    url(r'^view_all', views.mongo_view, name="view")
]
