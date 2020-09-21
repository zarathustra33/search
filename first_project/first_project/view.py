from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    # return HttpResponse('About')
    return render(request,'homepage.html')

def homepage(request):
    # return HttpResponse('Sharon"s Home')
    return render(request,'about.html')