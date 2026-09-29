# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import Member
from django.template import loader
from .custom import Bike,Motorcar


def members_list(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('register.html')
    context= {
    'mymembers' : mymembers ,
    }
    return HttpResponse(template.render(context,request))


def my_view(request):
    data = Member.objects.filter()
    return render(request, 'register.html', {'results':data})

def vehicle_view(request):
    bike = Bike()
    motorcar = Motorcar()
    #output= f"Bike Model: {bike.model} <br> Motorcar Name: {motorcar.name} <br> Method call: {motorcar.display()}" 
    return render(request, 'vehicle.html')
 
def lookbook(request):
    return render(request, 'lookbook.html')

def home(request):
    return render(request, 'index.html')
def Recipie(request):
    return render(request, 'recipie.html')
 
def exhibition(request):
    return render(request, 'ex.html')
def exh(request):
    return render(request, 'exh.html')
def exhi(request):
    return render(request, 'exhi.html')
def exhibition4(request):
    return render(request, 'ex(4).html')
def exhibition5(request):
    return render(request, 'ex(5).html')
def exhibition6(request):
    return render(request, 'ex(6).html')
def exhibition7(request):
    return render(request, 'ex(7).html')

def color(request):
    return render(request, 'color.html')

def image(request):
    return render(request,'images.html')    

def current(request):
    return render(request, 'current.html')

 