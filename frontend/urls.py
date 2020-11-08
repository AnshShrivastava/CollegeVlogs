from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="Home"),
    path("home",views.home,name="Home"),
    path("test",views.test,name="test"),
    path("newrequest",views.newrequest,name="Requests"),
    path("about",views.about_us,name="About Us"),
    path("contact",views.leads,name="Contact Us"),
    path("institutes",views.institutes,name="Institutes"),
    path("vloggers",views.vloggers,name="Vloggers"),
    path("vlogs",views.vlogs,name="Vlogs"),
    path("vloglist",views.vloglist,name="Vlogs"),
    path("layout",views.layout,name="layout"),
    path('search1',views.search.as_view(),name='Search'),
    path('college', views.college, name="College"),
    path('thank', views.thank, name="thank")
]
