from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def display_topics(request):
    QSTO=Topic.objects.all()
    QSTO=Topic.objects.all().order_by('topic_name')
    QSTO=Topic.objects.all().order_by('-topic_name')
    # QSTO=Topic.objects.get(topic_name='Cricket').order_by()
    QSTO=Topic.objects.all().order_by(Length('topic_name'))
    QSTO=Topic.objects.all().order_by('-topic_name')
    QSTO=Topic.objects.exclude(topic_name='Cricket')
    QSTO=Topic.objects.filter(topic_name='Badminton')
    
    
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
    QSWO=webpage.objects.all().order_by('name')
    QSWO=webpage.objects.filter(topic_name='Cricket').order_by('name')
    QSWO=webpage.objects.all().order_by(Length('name'))
    QSWO=webpage.objects.all().order_by('-name')
    QSWO=webpage.objects.exclude(topic_name='Football')
    QSWO=webpage.objects.filter(name__startswith='V')
    QSWO=webpage.objects.filter(url__endswith='com')
    QSWO=webpage.objects.filter(name__contains='i')
    QSWO=webpage.objects.filter(name__contains='a')
    QSWO=webpage.objects.filter(Q(name__contains='i')& Q(url__endswith='com'))
    QSWO=webpage.objects.filter(Q(name__contains='i') | Q(url__endswith='com'))
    


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
    QSAO=Access_Records.objects.all().order_by('author')
    # QSAO=Access_Records.objects.filter(name='Virat kohli').order_by('author')
    QSAO=Access_Records.objects.all().order_by(Length('author'))
    QSAO=Access_Records.objects.all().order_by('-author')
    QSAO=Access_Records.objects.filter(date__gt='2023-08-26')
    QSAO=Access_Records.objects.filter(date__gte='2023-08-26')
    QSAO=Access_Records.objects.filter(date__lt='2023-08-26')
    QSAO=Access_Records.objects.filter(date__lte='2023-08-26')
    QSAO=Access_Records.objects.filter(date__month__lte='08')
    QSAO=Access_Records.objects.filter(date__day__lte='20')
    QSAO=Access_Records.objects.filter(date__year__gte='2023')
    
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


    