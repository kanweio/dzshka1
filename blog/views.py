from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

def main(request):
    if request.method == 'GET':
        return HttpResponse('Hello')


def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello, its my project!')


def now_data(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now())


def bye(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye!')
