from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,"index.html")

def Home(request):
    return render(request,"home.html")

def Reg(request):
    return render(request,"reg.html")