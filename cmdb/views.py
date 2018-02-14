from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models
# Create your views here
# to animating the dynamical file , give a predefined dictionary for returning
user_list = [
    {"user":"jack","pwd":"abc"},
    {"user": "tom", "pwd": "ABC"},
]

def index(request):
    # request.POST
    # request.GET
    ################################################
    # return HttpResponse("Hello World!")
    ################################################
    # use render function when you want to return a html file
    # return render(request,"index.html")#the first parameter is fixed, the second parameter is the html file you want to return
    ################################################
    # if(request.method=="POST"):
    #     username = request.POST.get("username",None)
    #     password = request.POST.get("password",None)
    #     print(username,password)
    # return render(request,"index.html")
    ################################################
    # return dynamical file
    # if request.method == "POST":
    #     username = request.POST.get("username",None)
    #     password = request.POST.get("password",None)
    #     temp = {"user":username,"pwd":password}
    #     user_list.append(temp)
    # return render(request,"index.html",{"data":user_list})  #data is the pointer for referencing in the html file

    ################################################
    # using database
    if request.method=="POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)

        # add items into db
        models.UserInfo.objects.create(user=username,pwd=password)
    # read items from db
    user_list = models.UserInfo.objects.all()

    return render(request,"index.html",{"data":user_list})
