from django.http import HttpResponse
from django.shortcuts import render
from .models import inmakesdata
from .models import team
# Create your views here.


def demo(request):
    obj=inmakesdata.objects.all()
    obj2=team.objects.all()
    return render(request,'index.html',{'result':obj,'teamobject':obj2})

