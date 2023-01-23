from django.shortcuts import render
import folium 
from folium import plugins
import geocoder
from .forms import UserRegistration
from .models import User
from .models import Addresse


# Create your views here.

def index(request):

    #creation de la carte
    m = folium.Map(location = [50,-5])

    l = plugins.LocateControl(auto_start=True)
    l.add_to(m)
    print (l)
    
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
            reg = User(name=nm,password=pwd,groupe=grp)
            fm.save()
            fm = UserRegistration()
    else :
        fm = UserRegistration()
    return render(request,'connect.html',{'form':fm})


def map (request):
    #addresse = Addresse.objects.all().last()
    loca = geocoder.osm('UK')
    lat = loca.lat
    lng = loca.lng
    g = geocoder.ip('me')
    print(g.latlng)
    #contry = loca.contry
    m = folium.Map(location = [50.8505, 4.3488])
    folium.Marker(g.latlng).add_to(m)
    m = m._repr_html_()
    context = {
        'm':m,
    }
    return render(request,'map.html',context,)
    

def head (request):
    return render(request,'head.html')


def about(request):
    return render(request,'about.html')


def deconect(request):

    return render(request,'deconect.html')

