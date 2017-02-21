from django.conf.urls import url, include

import apps.jobTrackerWebapp.views as views

urlpatterns = [
    url(r'^$', views.rest_index, name='rest_index'),
    url(r'^get_job/(?P<job_id>[A-z0-9-]+)$', views.mongo_get_job, name="get_job"),
    url(r'^get_jobs', views.mongo_get_all_jobs, name="get_all_jobs"),
    url(r'^update_job/(?P<server_id>[A-z0-9-\'\s]+)$', views.mongo_update_job, name="update_job")
]
