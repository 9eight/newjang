from django.shortcuts import render, get_object_or_404
# from apps.blog.models import Blog
from .models import Blog

# Create your views here.


def index(request):
    blogs = Blog.objects.order_by('-pub_date')
    context = {'blogs': blogs}

    return render(request, 'blog/index.html', context)

def post(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {'blog': blog}
    return render(request, 'blog/post.html', context)


def by_month(request, month_id):
    blogs = Blog.objects.filter(pub_date__month=month_id)
    context = {'blogs': blogs}

    return render(request, 'blog/all_posts.html', context)
