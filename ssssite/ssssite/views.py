from django.shortcuts import render
from django.http import HttpResponse


def welcomeurl(request):
    print(request)
    return HttpResponse("<b><h1>Welcome to my site!</h1></b>")
