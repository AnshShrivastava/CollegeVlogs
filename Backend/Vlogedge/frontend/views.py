from django.shortcuts import render,redirect
from api.models import *
from rest_framework import views
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import HttpResponse
# Create your views here.

def home(request):
    data = Vlogs.objects.all()

    return render(request,'index.html',{'info': data})

def leads(request):
    # if request.method=="POST":
    #     name = request.POST["name"]
    #     email = request.POST["email"]
    #     collegeemail = request.POST["collegeemail"]
    #     collegename = request.POST["collegename"]
    #     request = request.POST["request"]        
    #     lead = Leads(name=name,college=collegename,email=email,college_email=collegeemail,request=request)
    #     lead.save()

    return render(request,"contact-us.html")

def newrequest(request):
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        collegename = request.POST["collegename"]
        requests = request.POST['requests']
        filenew = request.FILES['filenew']
        fs = FileSystemStorage()
        filename = fs.save(filenew.name, filenew) 
        req = Requests(name=name,college=collegename,email=email,file=fs.url(filename),request=requests)
        req.save()
        
    return render(request,"index.html",)


def about_us(request):
    return render(request,'about-us.html')

def vlogs(request):
    vlog_id = request.GET.get('vlog_id')
    v = Vlogs.objects.get(id=vlog_id) 
    return render(request,'postview.html',{'data':v})

def layout(request):
    return render(request,'layouts.html')

class search(views.APIView):
    pass
