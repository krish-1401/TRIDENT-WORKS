from django.shortcuts import render,redirect
# Create your views here.
from django.contrib.auth.models import User
from .forms import Profile_form
from .models import Profile
def main(request):
    return render(request,'main/main.html',{})

def index_main(request):
    return render(request,'main/index_main.html',{})

def about(request):
    return render(request,'main/about.html',{})

def cleaner(request):
    cleaner_list=Profile.objects.filter(profession="Cleaner")
    return render(request,'main/Cleaner.html',{'cleaner_list':cleaner_list})

def cook(request):
    cook_list=Profile.objects.filter(profession="Cook")
    return render(request,'main/Cook.html',{'cook_list':cook_list})

def plumber(request):
    plumber_list=Profile.objects.filter(profession="Plumber")
    return render(request,'main/Plumber.html',{'plumber_list':plumber_list})

def elec(request):
    elec_list=Profile.objects.filter(profession="Electrician")
    return render(request,'main/Electrician.html',{'elec_list':elec_list})

def carp(request):
    carp_list=Profile.objects.filter(profession="Carpenter")
    return render(request,'main/carpenter.html',{'carp_list':carp_list})

# def login_0(request):
#     form=Profile_form(request.POST or None)
#     if form.is_valid():
#         profile=form.save(commit=False)
#         profile.user_name=request.user
#         profile.save()
#         return redirect('index')
    
#     return render(request,'main/login_0.html',{'form':form})
def login_0(request):
    if request.method == 'POST':
        gender=request.POST.get('gender')
        email = request.POST.get('email')
        age = request.POST.get('age')
        city = request.POST.get('city')
        profession = request.POST.get('profession')
        mobile = request.POST.get('mobile')
        fees=request.POST.get('fees')
        
        # Create a new Profile object and save it to the database
        profile = Profile(user_name=request.user, email=email, age=age, city=city, profession=profession, mobile=mobile,fees=fees,gender=gender)
        profile.save()
        
        return redirect('index')

    # If the request method is not POST or form is not valid, render the template with the form
    form = Profile_form()
    return render(request, 'main/login_0.html', {'form': form})
