from django.shortcuts import render
from blog.models import *
# Create your views here.


def index(request):
    """show blogs' list"""
    blogs = Blog.objects.all()
    return render(request, '../templates/index.html', locals())


def gallery(request):
    return render(request, '../templates/gallery.html', locals())


def contact(request):
    return render(request, '../templates/contact.html', locals())


def blog(request):
    return render(request, '../templates/blog.html', locals())