from django.shortcuts import render
from .models import Posts
# Create your views here.

def index(request):
    datas = Posts.objects.all()
    

    return render(request, 'home/index.html',{'datas':datas})

def detail(request,id):
    
    post=Posts.objects.get(id=id)
    return render(request, 'home/detail.html',{'post': post})