from django.shortcuts import render
from .models import Profile, Image,Comment
# Create your views here.
def index (request):
    title = 'gram :-)'
    current_user = request.user
    profile = Profile.get_profile()
    image = Image.get_images()
    comments = Comment.get_comment()
    
    
    
    
    return render(request, 'index.html',{"title":title,
                                        "profile":profile,
                                        "comments":comments,
                                        "current_user":current_user,
                                        "images":image,})
