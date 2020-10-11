from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="Home"),
    path("newrequest",views.newrequest,name="Requests"),
    path("aboutus",views.about_us,name="About Us"),

]
