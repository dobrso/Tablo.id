from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import PostForm
from .models import Post

def post_list(request):
    posts = Post.objects.all()

    context = {'posts': posts}

    return render(request, 'posts/post_list.html', context)

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post_list')
    else:
        form = PostForm()

    context = {'form': form}

    return render(request, 'posts/post_create.html', context)

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'posts/post_detail.html', context)

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', post_id=post_id)
    else:
        form = PostForm(instance=post)

    context = {'form': form}
    return render(request, 'posts/post_edit.html', context)

@login_required
def post_delete(request, post_id):
    pass