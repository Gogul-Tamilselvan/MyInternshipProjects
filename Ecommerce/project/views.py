from http.client import HTTPResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from .forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout

def home(request):
     products=Product.objects.filter(trending=1)
     return render(request,"index.html",{"products":products})

def register(request):
        form=CustomUserForm()
        if request.method=='POST':
            form=CustomUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Registration Success You can Login Now..!")
                return redirect('login')
        return render(request,"register.html",{'form':form})

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
       if request.method=='POST':
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in Successfully")
            return redirect("/")
        else:
            messages.error(request,"Invalid User Name or Password")
            return redirect("/login")
    return render(request,"login.html")

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logged out Successfully')
    return redirect('/')


def collection(request):
    catagory = Catagory.objects.filter(status=0) 
    return render(request,'collection.html',{'catagory':catagory})


def collectionview(request,name):
    if(Catagory.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name=name)
        return render(request,"product_index.html",{"products":products,"category_name":name})
    else:
        messages.warning(request,"No Such Catagory Found")
        return redirect('collection')
    
def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(Catagory.objects.filter(name=cname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"product_details.html",{"products":products})
        else:
            messages.warning(request,"No Such Product Found")
            return redirect('collection')
    else:
        messages.warning(request,"No Such Catagory Found")
        return redirect('collection')
  
