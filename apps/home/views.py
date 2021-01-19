from django.shortcuts import render, get_object_or_404
from apps.blog.models import Blog
# from .models import Blog


def index(request):
    blogs = Blog.objects.order_by('-pub_date')
    context = {'blogs': blogs}

    return render(request, 'home/index.html', context)

def contact_us(request):
    return render(request, 'home/contact_us.html')

def about(request):
    return render(request, 'home/about.html')
