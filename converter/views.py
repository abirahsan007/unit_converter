from django.shortcuts import render
from django.http import HttpResponse
from .models import AllData
from datetime import datetime



def dashboard(request):
  context = {
     'datas' : AllData.objects.all(),
     'title': 'Unit Converter Tool',
      'time' : datetime.now
  }
  return render(request, 'converter\dashboard.html', context)

def convertPage(request):
  context = {
     'title': 'Unit Converter Tool'
  }
  return render(request, 'converter\page2.html', context)
# Create your views here.
