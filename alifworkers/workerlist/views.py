from django.shortcuts import render
#from django.http import HttpResponse
from django.conf import settings

def homepage(request):
    return render(request, 'workerlist/index.html')