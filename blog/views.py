from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return render(request, "about.html")
    return HttpResponse("WELOCME in blog home page.")


def about(request):
    return HttpResponse("Welcome to about page.")
