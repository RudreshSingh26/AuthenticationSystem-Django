from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth import logout , authenticate , login

def index(request):
    print(request.user) 
    if request.user.is_anonymous:    
        return redirect("/userlogin")           
    return render(request,'index.html')

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'userlogin.html')    
    return render(request,'userlogin.html')
    
def userlogout(request):
    logout(request)
    return redirect('/userlogin')
