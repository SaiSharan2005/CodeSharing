from django.shortcuts import render,redirect
from django.http import HttpResponse
from  . models import Room
# Create your views here.
def home(request):
    rooms = Room.objects.all()
    # if len(rooms.Question)>50:
    #     rooms.Question = rooms.Question[:50]
    # else:
    #     pass

    context = {'rooms':rooms}
    
    # return HttpResponse('Home Page')
    return render(request,"codes/home.html",context)

def room(request,pk):
    rooms = Room.objects.get(id=pk)
    context = {'room':rooms}
    return render(request,"codes/room.html",context)


