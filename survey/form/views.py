from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def form(request):
    return HttpResponse('<h3>Survey Form</h3>')

def index(request):
    return render(request,'index.html')
def survey(request):
    return render(request,'survey.html')    
    
