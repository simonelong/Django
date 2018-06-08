from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse

from django.http import HttpResponse,JsonResponse

from models import *
import os


def index(request):
    return render(request,'booktest/index.html')


def uploadPic(request):
    return render(request,'booktest/uploadpic.html')


def uploadHandle(request):
    f1=request.FILES['pic1']
    fname =os.path.join(settings.MEDIA_ROOT,f1.name)
    with open(fname,'w') as pic:
        for b in f1.chunks():
            pic.write(b)
    context ={'imgurl':f1.name}
    #return HttpResponse(f1.name)
    return render(request,'booktest/imageshow.html',context)



#sheng shi qu

def area(request):
    return render(request,'booktest/area.html')

def sheng(request,id):
    id1 =int(id)
    if id1 ==0 :
        data =AreaInfo.objects.filter(parea__isnull=True)
    else :
        data=[{}]
    list =[]
    for area in data:
        list.append([area.id,area.title])
    return JsonResponse({'data':list})


def shi(request):
    pid =request.GET.get('pid')
    slist =AreaInfo.objects.filter(parea_id=pid)
    if slist:
        list =[]
        for s in slist:
            list.append({'id':s.id,'title':s.title})
    return JsonResponse({'data':list})

def qu(request):
    pid = request.GET.get('pid')
    slist = AreaInfo.objects.filter(parea_id=pid)
    if slist:
        list = []
        for s in slist:
            list.append({'id': s.id, 'title': s.title})
    return JsonResponse({'data': list})