from django.shortcuts import render,redirect
from api.models import *
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'index.html')

def leads(request):
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        collegeemail = request.POST["collegeemail"]
        collegename = request.POST["collegename"]
        request = request.POST["request"]        
        lead = Leads(name=name,college=collegename,email=email,college_email=collegeemail,request=request)
        lead.save()

    return redirect("/")

def newrequest(request):
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        collegename = request.POST["collegename"]
        requests = request.POST['requests']
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile) 
        req = Requests(name=name,college=collegename,email=email,file=fs.url(filename),request=requests)
        req.save()

    return render(request,"index.html")


def about_us(request):
    return render(request,'about-us.html')
