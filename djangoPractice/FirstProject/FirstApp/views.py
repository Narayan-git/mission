from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    s="<center><h1>Welcome to Django</h1></center>"
    return HttpResponse(s)
def second(request):
    s = "<center><h1>This is Second Page</h1></center>"
    return HttpResponse(s)

import datetime

def main(request):
    time = datetime.datetime.now()
    h = int(time.strftime('%H'))
    msg = ""
    if h<12:
        msg = "Good Morning"
    elif h>=12 and h<=16:
        msg = "Good Afternoon"
    elif h>16 and h<=19:
        msg = "Good Evening"
    else:
        msg = "Good Night"

    MyDict = {"Name": "Narayan Sahu", "time": time, "msg" : msg}
    return render(request, "FirstApp/index.html", context= MyDict)
