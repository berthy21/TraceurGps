from django.shortcuts import render
import folium 
from folium import plugins

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
    return render(request,'index.html',context)