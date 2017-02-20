import ast
from django.shortcuts import render, reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .mongo import *
from django.views.decorators.csrf import csrf_exempt




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

def mongo_view_all_jobs(request):
    document = get_all_from_job_collection()
    return render(request, 'view_jobs.html', {'data': document})

# def mongo_insert_job(request):
#     insert_to_job_collection(request.GET['job_uuid'], request.GET['status'])
#     return HttpResponse("ok")

def mongo_get_job(request, job_id):
    document = get_from_job_collection(job_id)
    return HttpResponse(document)

def mongo_get_all_jobs(request):
    document = get_all_from_job_collection()
    return HttpResponse(document)

@csrf_exempt
def mongo_update_job(request, server_id):
    # job_complete = ast.literal_eval(list(request.POST.keys())[0])
    job_complete = ast.literal_eval(request.body.decode("utf-8"))
    job_dict = job_complete.get('job')
    job_uuid = job_dict.get('job_uuid')
    update_job(server_id, job_uuid, job_dict)
    return HttpResponse("ok")