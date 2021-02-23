from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=="POST":
        username=request.POST['username1']
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if request.user.is_authenticated:
                return redirect("/") #To redirect to the home page of the application
        else:
            return redirect('login')
            print("Failed")
def register(request):
    if request.method=="GET":
        return render(request,'register.html')
    elif request.method=="POST":
        name = request.POST['name']
        username = request.POST['username']
        email1 = request.POST['email1']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("Username taken")
                return redirect("register")
            elif User.objects.filter(email=email1).exists():
                print("Email id taken")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username,first_name=name,email=email1,password=password1)
                user.save()
                print("User created")
                return redirect('login')

