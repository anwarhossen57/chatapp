
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse

def home(rep):
    return HttpResponse("This is home page")
def about_user(rep):
    return HttpResponse("This is about            page")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("about/", about_user),
]
