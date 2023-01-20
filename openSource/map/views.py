from django.shortcuts import render
import folium 
from folium import plugins
from .forms import UserRegistration
from .models import User

# Create your views here.

def index(request):

    #creation de la carte
    m = folium.Map(location = [50,-5])

    plugins.LocateControl(auto_start=True).add_to(m)
    
    folium.Marker()
    #la representation html de l'objet carte 
    m =  m._repr_html_()
    context = {
        'm':m,
    }
    return render(request,'index.html',context,)


def connect(request):
    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            pwd = fm.cleaned_data['password']
            grp = fm.cleaned_data['groupe']
            reg = User(name=nm,password=pwd,group=grp)
            fm.save()
            fm = UserRegistration()
    else :
        fm = UserRegistration()
    return render(request,'connect.html',{'form':fm})


def map (request):
    return render(request,'map.html')

def head (request):
    return render(request,'head.html')


def about(request):
    return render(request,'about.html')


def add_show(request):

    return render(request,)

