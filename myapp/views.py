from django.shortcuts import render

# Create your views here.

def app(request):
    return render(request,'app.html')

def courses(request):
    return render(request,'courses.html')

def bootcamp(request):
    return render(request,'bootcamp.html')

def requestcall(request):

    return render(request,'requestcall.html')

def signin(request):
    return render(request,'signin.html')

def login(request):
    return render(request,'login.html')



