from asyncio.windows_events import NULL
from django import forms
import uuid
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from django.contrib.messages import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.messages import constants as messages
from requests import delete, request
from .models import inputs
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# MESSAGE_TAGS = {
#     messages.ERROR: 'danger'
# }
# Create your views here.

def home(request):
    return HttpResponse("Hello I am Working")

def logins(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        password = request.POST.get('password')
        # user = authenticate(username=uname, password=password)
        users = User.objects.all()
        print(users)
        for i in users:
            print(i)
            if uname == '':
                return render(request, "login.html")
            if uname == i.username:
                if password == i.password:
                    return redirect('travel')
                else:
                    # messages.SUCCESS(request, "Invalid Password")
                    print('wtfs')
                    return render(request, "login.html")
        # else: # This else statement is out of for coz it will execute when the user is not found in the database
        #     return render(request, "login.html")
    return render(request, "login.html")
    # return render(request, "go.html")



def register(request):
    if request.method == "POST":
        uname = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=uname, password=password, email=email)
        user.save()
        print("User Created")
    return render(request, "index.html")
    
    # if request.method == 'POST':
    #     uname = request.POST['username']
    #     email = request.POST['email']
    #     pass1 = request.POST['password']
    #     pass2 = request.POST['repassword']
    #     user  = User(username=uname, email=email, password=pass1)
    #     user.save()
    #     print('******', user.email)
    #     if user.pk is not None:
    #         if pass1 == pass2:
    #             print("User created")
    #             return redirect('login')
    #     # messages.success(request, "Your entered data has been recorded succesfully!")
        # user = User.objects.create_user(username=uname, email=email, password=pass1)``
                
    # return render(request, 'index.html')
    
    

# from django.contrib.auth.decorators import user_passes_test
# @user_passes_test(lambda user: not user.is_authenticated())

def travel(request):
    if request.user.is_authenticated:
        print(request.user.is_authenticated)
        if request.method == "POST":
            uid = uuid.uuid1()
            time = request.POST["time"]
        
            destination = request.POST["browser"] # User input of destination
            inp = inputs(uid=uid, time=time, destination=destination)
            inp.save()
            dest = inputs.objects.values_list('destination')   # Database inputs for destinations
            dest_list = list(dest)
            
            
            for i in dest_list:
                print(i)
                print('This is dest:', dest_list)
                if i in dest_list:
                    # dest = inputs.objects.values_list('Thane')
                    if inputs.objects.filter(destination=destination).exists() == True:
                    # if inputs.objects.filter(destination=destination) == i:
                        qs = inputs.objects.filter(destination=destination).values()
                        print('I am ------', qs)
                    return render(request, "GO.html")
            return redirect('go')
    else:
        return redirect('login')
        
    return render(request, "home.html")

def go(request):
    name = request.user.username
    print("hi", name)
    uname = request.user.username
    # from django.contrib.auth import get_user_model
    # User = get_user_model()
    users = User.objects.all()
    print(users)
    for i in users:
        print(i)
        print("hi", uname)
        print(request.user)
    
    # u = User.objects.get(username = 'john')
    # u.delete()
    # print("The user is deleted")
    
    
    return render(request, "go.html")


