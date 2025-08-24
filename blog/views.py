# Inlocuieste tot continutul acestui fisier cu ce e mai jos

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
  
    users_who_liked = post.likes.all()
   
    liked = False
    if request.user.is_authenticated and request.user in users_who_liked:
        liked = True
    
    context = {
        'post': post,
        'liked': liked,
        'users_who_liked': users_who_liked
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