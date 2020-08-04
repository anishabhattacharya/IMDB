from django.shortcuts import render,redirect
from django.contrib import messages
from IMDB.settings import IMDB_FILE
import json
from app1.middleware import imdbweb

def adminloginpage(request):
    return render(request, "adminloginpage.html")

def adminvalidation(request):
    adminname=request.POST.get("a1")
    adminpassword=request.POST.get("a2")

    if adminname=="kamal" and adminpassword=="Kamal4321":
        return render(request, "adminwelcomepage.html", {"data":adminname})
         #return redirect("adminwelcomepage.html")
    else:
        messages.error(request,"Invalid User")
        return redirect("adminloginpage.html")


def adminwelcomepage(request):
    dict_data=json.loads(open(IMDB_FILE).read())
    print(dict_data)
    # id = [x for x in dict_data]
    return render(request, "adminwelcomepage.html", {'data':dict_data})


def openmovie(request):
    movid=request.GET.get("id")
    dict_data = json.loads(open(IMDB_FILE).read())
    return render(request,"actor.html",{"idi":movid,"result":dict_data[movid]})



def dummy(request):
    dict_data = json.loads(open(IMDB_FILE).read())
    print(dict_data)

    return render(request,"dummy.html",{'data':dict_data})