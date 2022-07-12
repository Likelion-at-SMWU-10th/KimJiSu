from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'tigerapp/index.html')

def about(request):
    return render(request, 'tigerapp/about.html')