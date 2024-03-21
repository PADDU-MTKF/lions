from django.shortcuts import render
from . import data as db
from django.http import HttpResponse
import os
from django.core.cache import cache
# Create your views here.


def update():
    pass

def cache(request):
    cache.set("cachename","data",timeout=None)
    return HttpResponse(status=200)


def home(request):

    # db.getDocument(os.getenv("DB_ID"),"xfsdfedsf",)

    data={
        "our_prind":cache.get("ourpride"),
    }

    return render(request,'home.html'data=data)

# def home(request):
#     if(request.method=="POST"):


def about(request):
    return render(request,'about.html')


def event(request):
    if(request.method=="POST"):
        if "nameSearchbtn" in request.POST:
            search_value = request.POST.get("searchText")
            return render(request, 'eventdetails.html', {'search_value': search_value})
        elif "dateSearchbtn" in request.POST:
            to_date = request.POST.get("startDate")
            from_date = request.POST.get("endDate")
        elif "detailView" in request.POST:
            det_title = request.POST.get("etitle")
            det_date = request.POST.get("edate")
            det_dis = request.POST.get("edis")
            det_cvr = request.POST.get("ecvr")
            return render(request,'eventdetails.html',{'det_title':det_title,'det_date':det_date,'det_dis':det_dis,'det_cvr':det_cvr})
        
    
    else:
        data=[{'title':'Oscar Award','description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','date':'22-Mar-2002','cvr':'https://images.pexels.com/photos/772803/pexels-photo-772803.jpeg?auto=compress&cs=tinysrgb&w=600'},
              {'title':'title2','description':'dis2','date':'69','cvr':'https://images.pexels.com/photos/1770809/pexels-photo-1770809.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'},{'title':'Oscar Award','description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','date':'22-Mar-2002','cvr':'https://cloud.appwrite.io/v1/storage/buckets/65f1cac29e266939493a/files/65f959ba4d968516ae2d/view?project=65e1b46b94ff79f18974'},]
        return render(request,'event.html',{'data': data})
    

# def event(request):
#     if(request.method=="POST"):
#         return render(request,'eventdetails.html')
    
#     else:
#         return render(request,'event.html')