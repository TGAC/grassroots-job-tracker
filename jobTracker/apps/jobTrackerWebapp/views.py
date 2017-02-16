from django.shortcuts import render, reverse
from django.conf import settings
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .mongo import insert_to_test_collection, get_all_from_test_collection




# Create your views here.
def index(request):

    x = dict()

    x['items'] = ['abc', 'def', 'ghi']
    x['title'] = "Goodbye World"

    return render(request, 'index.html', {'data': x})


def mongo_insert(request):
    insert_to_test_collection({"name": request.GET['name'], "age": request.GET['age']})
    return HttpResponseRedirect(reverse("view"))

def mongo_view(request):
    document = get_all_from_test_collection()
    return render(request, 'mongo_test.html', {'data': document})
