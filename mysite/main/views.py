from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index_welcome(request):
    return HttpResponse("<h1>Welcome to Nature search!<h1> Click here to continue")

def index_home(request):
    # t = loader.get_template("mysite/templates/index.html")
    return render(request, "index.html")

def index_about(request):
    return render(request, "about.html")

def index_retrieval_result(request):
    return render(request, "retrieval.html")
