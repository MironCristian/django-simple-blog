from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post



def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    prima_postare = posts.first() # Luam doar prima postare
    if prima_postare:
        print("---------------------------------")
        print("Obiectul Post:", prima_postare.title)
        print("Accesand campul .likes:", prima_postare.likes)
        print("Rezultatul de la .likes.count():", prima_postare.likes.count())
        print("Rezultatul de la metoda .total_likes():", prima_postare.total_likes())
        print("---------------------------------")
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):    
    post = get_object_or_404(Post, pk=pk)
    liked = False 
    if request.user.is_authenticated and post.likes.filter(id=request.user.id).exists():
        liked = True    
        
    context = {
    'post': post,
    'liked': liked


    }

    return render(request, 'blog/post_detail.html', context)

@login_required

def like_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

  
    return redirect('post_detail', pk=post.pk)





