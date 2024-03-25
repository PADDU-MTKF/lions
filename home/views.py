from django.shortcuts import render
from . import data as db
from appwrite.query import Query
from django.http import HttpResponse
import os
from appwrite.client import Client
from django.core.cache import cache
import threading
# Create your views here.


def update():
    print("cache start")
    our_school=db.getDocument(os.getenv("DB_ID"),os.getenv("OUR_SCHOOL"))[0]
    present_trustee=db.getDocument(os.getenv("DB_ID"),os.getenv("PRESENT_TRUSTEE"))[0]
    our_pride=db.getDocument(os.getenv("DB_ID"),os.getenv("OUR_PRIDE"))[0]
    achives=db.getDocument(os.getenv("DB_ID"),os.getenv("ACHIEVEMENTS_AND_EXTRAS"),[Query.limit(100)])[0]

    cache.set("our_school",our_school,timeout=None)
    cache.set("present_trustee",present_trustee,timeout=None)
    cache.set("our_pride",our_pride,timeout=None)
    cache.set("achives",achives,timeout=None)
    print("cache ended")
    





async def updateCache(request):
    # Handle the request asynchronously without returning any response immediately
    thread = threading.Thread(target=update)
    thread.start()
    

    return HttpResponse(status=200)


def home(request):

    present_trustee=cache.get("present_trustee") 
    if present_trustee is None:
        update()
    present_trustee=cache.get("present_trustee") 
    our_pride=cache.get("our_pride")
    achives=cache.get("achives")
    
    # print(our_school)
    data = {
        "presentTrustee": present_trustee,
        "ourPride":our_pride,
        "achive":achives
    }
    return render(request,'home.html',data)




def about(request):
    our_school=cache.get("our_school") 
    if our_school is None:
        update()
    our_school=cache.get("our_school") 
    data={
        "our_school": our_school
    }

    return render(request,'about.html',data)


def event(request):
    if(request.method=="POST"):
        # if "nameSearchbtn" in request.POST:
        #     search_value = request.POST.get("searchText")
        #     return render(request, 'eventdetails.html', {'search_value': search_value})
        # elif "dateSearchbtn" in request.POST:
        #     to_date = request.POST.get("startDate")
        #     from_date = request.POST.get("endDate")
        if "detailView" in request.POST:
            det_title = request.POST.get("etitle")
            det_date = request.POST.get("edate") if request.POST.get("edate")!="None" else None
            det_dis = request.POST.get("edis") 
            det_cvr = request.POST.get("ecvr") if request.POST.get("ecvr")!="None" else None
            eimg1 = request.POST.get("eimg1") if request.POST.get("eimg1")!="None" else None
            eimg2 = request.POST.get("eimg2") if request.POST.get("eimg2")!="None" else None
            eimg3 = request.POST.get("eimg3") if request.POST.get("eimg3")!="None" else None
            
            data={'det_title':det_title,'det_date':det_date,'det_dis':det_dis,'det_cvr':det_cvr,'eimg1':eimg1,'eimg2':eimg2,'eimg3':eimg3}
            return render(request,'eventdetails.html',data)
        
        else:
            achive=cache.get("achives") 
            if achive is None:
                update()
            achive=cache.get("achives") 
            data={
                "achives": achive
            }
            return render(request,'event.html',data)
        
    
    else:
        achive=cache.get("achives") 
        if achive is None:
            update()
        achive=cache.get("achives") 
        data={
            "achives": achive
        }
        return render(request,'event.html',data)
    

# def event(request):
#     if(request.method=="POST"):
#         return render(request,'eventdetails.html')
    
#     else:
#         return render(request,'event.html')