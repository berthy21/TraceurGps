from django.shortcuts import render
import folium 
from folium import plugins
import geocoder
from .forms import UserRegistration
from .models import User,Member
import csv
import pandas as pd
from django.db.models import Q

i = 0


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
        i=2
    elif len (result)>1:
        print ("user exist deja")
        i=2
    else :
        u.save()
        print ("user is unique")
    count = Member.objects.all().count()


    print(i)
    g = geocoder.ip('me')
    m = folium.Map(location = [50.8505, 4.3488])
    folium.Marker(g.latlng).add_to(m)

    
    m = m._repr_html_()
    context = {
        'm':m,
    }

    if(i==2):
        print(i)

        nom_colonnes =['latitude','longitude']
        f= open ('localisation.csv','w') 
        with f:
            data = csv.DictWriter(f,delimiter="," ,fieldnames=nom_colonnes)
            data.writerow([g.lat,g.lng])
        f.close()

        da = pd.read_csv('localisation.csv')
    

        loc = da[['latitude',5]]
        folium.Marker(loc).add_to(m)




   

            


    return render(request,'map.html',context,)
    

def head (request):
    return render(request,'head.html')


def about(request):
    return render(request,'about.html')


def deconect(request):

    return render(request,'deconect.html')

