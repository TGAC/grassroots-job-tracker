from django.conf.urls import url, include

import apps.jobTrackerWebapp.views as views

urlpatterns = [
    url(r'^$', views.rest_index, name='rest_index'),
    url(r'^view_jobs', views.mongo_view_all_jobs, name="view_all_jobs"),
    url(r'^get_job/(?P<job_id>[a-f0-8-]+)$', views.mongo_get_job, name="get_job"),
    url(r'^get_jobs', views.mongo_get_all_jobs, name="get_all_jobs"),
    url(r'^update_job/(?P<server_id>[A-z0-9-\s]+)$', views.mongo_update_job, name="update_job")
]
