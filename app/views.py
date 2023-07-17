from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse


def insert_topic(request):
    TMFO=TopicModelForm()
    d={'TMFO':TMFO}
    if request.method=='POST':
        TMFD=TopicModelForm(request.POST)
        if TMFD.is_valid():
            TMFD.save()
            return HttpResponse('insert topics')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WMFO=WebpageModelForm()
    d={'WMFO':WMFO}
    if request.method=='POST':
        WMFD=WebpageModelForm(request.POST)
        if WMFD.is_valid():
            WMFD.save()
            return HttpResponse('insert_webpage')


    return render(request,'insert_webpage.html',d)



def insert_Acess(request):
    AMFO=AccessModelForm()
    d={'AMFO':AMFO}
    if request.method=='POST':
        AMFD=AccessModelForm(request.POST)
        if AMFD.is_valid():
            AMFD.save()
            return HttpResponse('insert_Acess')


    return render(request,'insert_Acess.html',d)

