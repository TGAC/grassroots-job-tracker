from django.shortcuts import render, reverse
from django.conf import settings
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .mongo import *




# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def rest_index(request):
    return render(request, 'rest_index.html', {})


def mongo_insert(request):
    insert_to_test_collection({"name": request.GET['name'], "age": request.GET['age']})
    return HttpResponseRedirect(reverse("view"))

def mongo_view(request):
    document = get_all_from_test_collection()
    return render(request, 'mongo_test.html', {'data': document})

def mongo_view_all_job(request):
    document = get_all_from_job_collection()
    return render(request, 'view_all_jobs.html', {'data': document})

def mongo_insert_job(request):
    insert_to_job_collection(request.GET['job_uuid'], request.GET['status'])
    return HttpResponse("ok")

def mongo_get_job(request):
    document = get_from_job_collection({"job_uuid": request.GET['job_uuid']})
    return HttpResponse(document)

def mongo_update_job(request):
    update_job(request.GET['job_uuid'], request.GET['status'])
    return HttpResponse("ok")