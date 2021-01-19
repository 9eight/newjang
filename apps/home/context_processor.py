from apps.blog.models import Blog

def extra(request):
    months = Blog.objects.dates('pub_date', 'month').order_by()

    return {'months': months}
