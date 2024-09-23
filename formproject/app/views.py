from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def formcreation(request):
    if request.method=='POST' :
        return HttpResponse('User has Submitted Data')
    return render(request,'formcreation.html')



def insert_topic(request):
    if request.method=='POST' :
        topics=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=topics)[0]
        TO.save()
        return HttpResponse('Topic is Created')
    return render(request,'insert_topic.html')



def insert_Webpage(request):
    QLWO=Topic.objects.all()
    d={'QLWO':QLWO}

    if request.method=='POST':
        TN=request.POST['topic']
        na=request.POST['name']
        ul=request.POST['url']
        em=request.POST['email']

        TO=Topic.objects.get(topic_name=TN)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ul,email=em)[0]
        WO.save()
        return HttpResponse('Webpage is Created')
        
    return render(request,'insert_Webpage.html',d)



def insert_accessrecord(request):
    QLAO=Webpage.objects.all()
    d1={'QLAO':QLAO}

    if request.method=='POST':
        TN=request.POST['name']
        ar=request.POST['author']
        dt=request.POST['date']

        TO=Webpage.objects.get(name=TN)
        AO=AccessRecord.objects.get_or_create(name=TO,author=ar,date=dt)[0]
        AO.save()
        return HttpResponse('AccessRecord is Created')
    
    return render(request,'insert_accessrecord.html',d1)



def select_topic(request):
    LTO=Topic.objects.all()
    d2={'LTO':LTO}

    if request.method=="POST":
        topics=request.POST.getlist('topics')
        print(topics)


        webpages=Webpage.objects.none()
        for tn in topics:
            webpages=webpages | Webpage.objects.filter(topic_name=tn)
        d3={'webpages':webpages}
        return render(request,'display_webpage.html',d3)

    return render(request,'select_topic.html',d2)


def checkbox(request):
    LCO=Topic.objects.all()
    d={'LCO':LCO}

    return render(request,'checkbox.html',d)


def update_webpage(request):

    #USING UPDATE METHOD
    Webpage.objects.filter(name='virat').update(email='ViralKohili@gmail.com')
    Webpage.objects.filter(topic_name='FootBall').update(email='footballindia@gmail.com')
    # Webpage.objects.filter(name='Ronald').update(topic_name='Kabbadi')
    Webpage.objects.filter(name='Raina').update(topic_name='Cricket') 
    Webpage.objects.filter(name='Ronald').update(topic_name='Cricket')
    Webpage.objects.filter(topic_name='Cricket').update(name='Bhubananeswar_kumar') 

    #USING GET_UPDATE_METHOD
    Webpage.objects.update_or_create(name='saniamirja',defaults={'url':'https://sm.in'})
    Webpage.objects.update_or_create(topic_name='Badmiton',defaults={'email':'Badmiton@gmail.com'})
    CTO=Topic.objects.get(topic_name='Cricket')
    Webpage.objects.update_or_create(name='	Bhubananeswar_kumar',defaults={'topic_name':CTO})
    Webpage.objects.update_or_create(name='Jyoti',defaults={'url':'http://India.com','topic_name':CTO})
    

    Webpages=Webpage.objects.all()
    d3={'Webpages':Webpages}
    
    
    return render(request,'display_webpage.html',d3)


def delete_webpage(request):
    Webpage.objects.filter(name='Bhubananeswar_kumar').delete()
    Webpage.objects.all().delete()
    Webpages=Webpage.objects.all()
    d1={'Webpages':Webpages}
    return render(request,'display_webpage.html',d1)