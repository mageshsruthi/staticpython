
from django.shortcuts import render
from .models import Place
from.models import Person

def demo(request):
    obj=Place.objects.all()
    obj1=Person.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

# Create your views here.
