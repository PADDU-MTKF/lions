from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def event(request):
    if(request.method=="POST"):
        return render(request,'eventdetails.html')
    else:
        return render(request,'event.html')

