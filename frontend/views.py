from django.shortcuts import render,redirect
from api.models import *
from rest_framework import views
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponse
from api.serializers import *

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
        
    return HttpResponse("Done");


def about_us(request):
    return render(request,'about-us.html')

def vlogs(request):
    vlog_id = request.GET.get('vlog_id')
    v = Vlogs.objects.get(id=vlog_id) 
    return render(request,'postview.html',{'data':v})

def layout(request):
    return render(request,'layouts.html')

class search(views.APIView):
    model = Vlogs,Vlogger,College
    serializer = VlogSerializer,VloggerSerializer,CollegeSerializer

    def get(self,request):
        string = request.GET['search']
        data = College.objects.filter(collegename__contains=string).distinct()
        # vlog = Vlogs.objects.filter(college_id__in = Vlogs.objects.values('college_id'))
        serializer = CollegeSerializer(data=data)
        serializer.is_valid()
        print(serializer['collegename'])
        return render(request,'searchresult.html')