from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topics(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)

def insert_topic(request):
    tn=input('Enter topic_name: ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpages.html',d)

def insert_webpage(request):
    tn=input('Enter topic_name: ')
    to=Topic.objects.get(topic_name=tn)
    n=input('Enter name: ')
    u=input('Enter url: ')
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpages.html',d)
def display_access_records(request):
    QSAO=Access_Records.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_access_records.html',d)

def Insert_Access_Records(request):
    pk=input('Enter a number:')
    d=input('Enter date:')
    a=input('Enter Author name:')
    wo=webpage.objects.get(pk=pk)
    ao=Access_Records.objects.get_or_create(name=wo,date=d,author=a)[0]
    ao.save()
    QSAO=Access_Records.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_access_records.html',d)


    