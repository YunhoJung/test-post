from django.shortcuts import render, redirect, get_object_or_404

from post.forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post_list.html', context)


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            Post.objects.create(
                comment=comment,
                author=request.user,
            )
            return redirect('post_list')
    else:
        form = PostForm()
    context = {
        'form': form
    }

    return render(request, 'post/post_create.html', context)


def post_delete(request, post_pk):
    if request.method == "POST":
        post = Post.objects.get(pk=post_pk)
        post.delete()
    return redirect('post:post_list')


def post_modify(request, post_pk):
        post = get_object_or_404(Post, pk=post_pk)
        if request.method == 'POST':
            form = PostForm(data=request.POST, files=request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = User.objects.first()
                post.save()
                return redirect('post_list')
        else:
            form = PostForm(instance=post)
        context = {
            'form': form
        }
        return render(request, 'post/post_modify.html', context=context)
