from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('<h1>This is the first page of Django Project</h1>')


def second(request):
    return HttpResponse('<h2>This is the second page of Django Project</h2>')


def third(request):
    return HttpResponse('<h3>This is the third page of Django Project</h3>')


def forth(request):
    return HttpResponse('<h4>This is the forth page of Django Project</h4>')


def fifth(request):
    return HttpResponse('<h5>This is the fifth page of Django Project</h5>')