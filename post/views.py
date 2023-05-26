from django.shortcuts import render

from .models import * 

# Create your views here.
def all(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    } 
    return render(request, 'post/all.html', context)
    

def single_post(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post, 
    }

    return render(request, 'post/single-post.html', context)
