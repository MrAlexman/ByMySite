from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse("HelloWorld")


def test(request):
    return HttpResponse("<h1>Тестовая страница</h1>")

