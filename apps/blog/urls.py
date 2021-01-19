# from apps.blog import views
from . import views
from django.urls import path

app_name = "blog"

urlpatterns = [
    path('', views.index, name="index_blog"),
    path('<int:blog_id>/post/', views.post, name="post"),
    path('<int:month_id>/month/', views.by_month, name="by_month"),
]
