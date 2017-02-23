import ast
from django.shortcuts import render, reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
import bson.json_util as json
from .mongo import *
from django.views.decorators.csrf import csrf_exempt




# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def rest_index(request):
    return render(request, 'rest_index.html', {})

def mongo_view_all_jobs(request):
    document = get_all_from_job_collection()
    return render(request, 'view_jobs.html', {'data': document})

def mongo_view_job(request, job_id):
    document = get_from_job_collection(job_id)
    return render(request, 'view_job.html', {'data': json.dumps(document)})

def mongo_get_job(request, job_id):
    document = get_from_job_collection(job_id)
    return HttpResponse(json.dumps(document))

def mongo_get_all_jobs(request):
    document = get_all_from_job_collection()
    return HttpResponse(json.dumps(document))

@csrf_exempt
def mongo_update_job(request, server_id):
    job_complete = ast.literal_eval(request.body.decode("utf-8"))
    job_dict = job_complete.get('job')
    job_uuid = job_dict.get('job_uuid')
    job_dict['server_id'] = server_id
    job_dict['timestamp'] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    response = update_job(job_collection).update({'job_uuid': job_uuid, "server_id": server_id}, {"$set":job_dict}, True)
    return HttpResponse(json.dumps(response))

def error404_handler(request):
    return HttpResponse("404", content_type='text/html; charset=utf-8', status=404)

def error500_handler(request):
    return HttpResponse("500", content_type='text/html; charset=utf-8', status=500)