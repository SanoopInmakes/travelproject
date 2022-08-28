from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['Email']
        password=request.POST['password']
        cpassword= request.POST['confirm_password']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save();

        else:
            messages.info(request,"password mismath")
            return redirect('register')
        return redirect('/')
    print("user created")

    return render(request,'userlogin.html')


def userlogin2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('userlogin2')
    return render(request, 'userlogin2.html')


def userlogin(request):
    if request.method=='POST' and 'signupbtn' in request.POST:
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['Email']
        password=request.POST['password']
        cpassword= request.POST['confirm_password']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")

                return redirect('userlogin')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('userlogin')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save();
                return redirect('userlogin2')
        else:
            messages.info(request,"password mismath")

            return redirect('userlogin')
    print("user created")


    if request.method=='POST' and 'signinbtn' in request.POST:
        loginname=request.POST['loginname']
        loginpass=request.POST['loginpass']
        user=auth.authenticate(username=loginname,password=loginpass)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
            # print("user logedim")
        else:
            messages.info(request,"invalid credentials")
            return redirect('userlogin2')

    # return render(request,'userlogin2.html')
    return render(request,'userlogin.html')


def logout(request):
    auth.logout(request)
    return redirect('/')