from django.shortcuts import HttpResponse

def my_fun(request):
    return HttpResponse('hello')

def my_name(request) :
    return HttpResponse('Ronak')