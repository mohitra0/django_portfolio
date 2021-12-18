from django.http.response import HttpResponse
from django.shortcuts import render
from .models import ProductConfig
def index(request):
    products=ProductConfig.objects.all()
    return render(request,'index.html',{'products' : products})
    # return HttpResponse('Hello world')


def new(request):
    return HttpResponse('new Products')
