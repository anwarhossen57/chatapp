from django.shortcuts import HttpResponse, render

def home(rep):
    return render(rep, 'home.html')
def about_user(rep):
    return render(rep, 'about.html')