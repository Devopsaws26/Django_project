from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello welcome to  delhi")


# Create your views here.
