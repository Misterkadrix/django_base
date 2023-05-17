from django.shortcuts import render

# Create your views here.

produits = [{"id":1,"produit":"fraise",'poids':'200gr','categorie':'fruits'},
            {"id":2,"produit":"banane","poids":"350gr","categorie":"fruits"},
            {"id":3,"produit":"amande","poids":"5gr","categorie":"noix"},
            {"id":4,"produit":"salade","poids":"100gr","categorie":"legumes"},]


def about(request):
    return render(request,'app/about.html')

def home(request):
    return render(request,'app/home.html')

def produit(request):
    return render(request,'app/produit.html',{'produits':produits})

def produit_detail(request,id):
    produit = produits[id-1]
    return render(request,'app/produit_detail.html',{'produit':produit})