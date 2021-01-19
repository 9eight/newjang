# from apps.home import views
from . import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', views.index, name="index"),
    path('contactus/', views.contact_us, name="contact_us"),
    path('about/', views.about, name="about"),
]


