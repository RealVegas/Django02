from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/lorem.html')

def info(request):
    return render(request, 'main/lorem_info.html')

def pan_eng(request):
    return render(request, 'main/eng_pangrams.html')

def pan_rus(request):
    return render(request, 'main/rus_pangrams.html')