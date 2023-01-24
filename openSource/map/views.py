from django.shortcuts import render
import geocoder
import folium 
from folium import plugins,PolyLine
from .forms import UserRegistration,AddresseReg
from .models import User,Member,Addresse
import csv
import pandas as pd
from django.db.models import Q
import geopy
from geopy.distance import distance



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
    membre = Member.objects.all()

    def get_ip(request):
        addr=request.META.get('http_X_FORWARDED_FOR')
        if addr :
            ip = addr.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_ip(request)
    u = Member(membre =ip)
    result = Member.objects.filter(Q(membre__icontains=ip))
    if(len(result)==1):
        print("user exist")
    elif len (result)>1:
        print ("user exist deja")
    else :
        u.save()
        print ("user is unique")
    count = Member.objects.all().count()


    g = geocoder.ip('me')
    m = folium.Map(location = [50.8505, 4.3488])
    folium.Marker(g.latlng,icon=folium.Icon(color='green')).add_to(m)
    print(ip)
    print(count)

    
    if request.method == 'POST':
        fm = AddresseReg(request.POST)
        if fm.is_valid():
            add = fm.cleaned_data['address']
            reg = Addresse(address=add)
            fm.save()
            fm = AddresseReg()
            print(add)
    else :
        fm = AddresseReg()

    add = Addresse.objects.all().last()
    location = geocoder.osm(add)
    lat = location.lat
    lon = location.lng

    print(add)
    folium.Marker(location.latlng).add_to(m)

    
    if(count==2 ): 
        print(count)
        g = geocoder.ip('me')
        #folium.Marker(g.latlng).add_to(m)

        nom_colonnes =['latitude','longitude']
        #f= open ('localisation.csv','w') 
        #with f:
         #   data = csv.DictWriter(f,delimiter="," ,fieldnames=nom_colonnes)
          #  data.writeheader()
            #data.writerow({'latitude':g.lat,'longitude':g.lng})
        #f.close()
#
        da = pd.read_csv('localisation.csv')
    

        loc = da[['latitude','longitude']]
        #folium.Marker(loc).add_to(m)

    km = distance(g.latlng,location.latlng)
    PolyLine([g.latlng,location.latlng],color='red').add_to(m)
    
    m = m._repr_html_()
    
    
    context = {
    'form':fm,
    'm':m,
    'km':km,
    }

    

    return render(request,'map.html',context)
    

def head (request):
    return render(request,'head.html')


def about(request):
    return render(request,'about.html')


def deconect(request):

    return render(request,'deconect.html')

