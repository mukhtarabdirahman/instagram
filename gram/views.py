from django.shortcuts import render
from .models import Profile, Image, Comment
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def welcome(request):
    return render(request,"base.html")

@login_required(login_url='/accounts/login/')
def home(request):
    posts = Image.get_all()
    
    return render(request, 'index.html', { 'posts': posts })

def post(request):
    posts = Image.get_all()
    
    return render(request, 'index.html', { 'posts': posts})






