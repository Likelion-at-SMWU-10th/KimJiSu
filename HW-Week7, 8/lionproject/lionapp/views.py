from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def home(request):
    return render(request, 'lionapp/home.html')

def blog(request):
    blogs = Blog.objects
    return render(request, 'lionapp/blog.html',{'blogs' : blogs })

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'lionapp/detail.html', {'blog': blog_detail})