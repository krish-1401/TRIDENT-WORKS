from django.shortcuts import render,redirect
# from .forms import RegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_tobe
from django.contrib.auth import logout as logout_tobe
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import random
# Create your views here.
from django.contrib.auth.models import User
import random
from .forms import RegisterForm 

# def register(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         # Check if user with this email already exists
#         if User.objects.filter(username=email).exists():
#             return render(request, 'user/register.html', {'error': 'Email is already registered'})

#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         mobile = request.POST.get('mobile')
#         profession = request.POST.get('profession')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         # profile=Profile.objects.get_or_create(profession=profession,mobile=mobile)
#         if password1 == password2:
#             user = User.objects.create_user(username=email, email=email, password=password1,
#                                             first_name=first_name, last_name=last_name)
#             # profile = Profile.objects.create(user=user, profession=profession, mobile=mobile)

#             return redirect('login')
#         else:
#             return render(request, 'user/register.html', {'error': 'Passwords do not match'})

#     return render(request, 'user/register.html')

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username=form.cleaned_data.get('username')
            # messages.success(request,f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form=RegisterForm()
    return render(request,'user/register.html',{'form':form})


def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login_tobe(request,user)
            return redirect('main:login_0')
        else:
            return redirect('login')
    else:
        return render(request,'user/login.html',{})
    

def index(request):
    return render(request,'user/index.html')