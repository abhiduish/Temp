from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from api.models import Stu
def save(request ,name,address,age, totalmarks):
    s = Stu(name=name,address=address,age=age,totalmarks=totalmarks)
    s.save()
    return HttpResponse('Post Query')

def get_all(request):
    s = Stu.objects.all()
    stu = [{i.name: i.totalmarks} for i in s]
    #response = ' , '.join(stu)
    return HttpResponse(stu)

def get_data(request,name):
    s = Stu.objects.get(name=name)
    stu=s.name," ",s.address,' ',s.age,' ',s.totalmarks
    return HttpResponse(stu)

def delete(request,name):
    s = Stu.objects.get(name=name)
    s.delete()
    return HttpResponse('Deleted Call')

def filter(request):
    s = Stu.objects.all()
    stu = [i.name for i in s if (i.totalmarks/5>=70)] 
    response = ' , '.join(stu)
    return HttpResponse(response)