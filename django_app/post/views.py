from django.shortcuts import render, redirect

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post_list.html', context)


def post_delete(request, post_pk):
    if request.method == "POST":
        post = Post.objects.get(pk=post_pk)
        post.delete()
    return redirect('post:post_list')


def post_modify(request, post_pk):
    if request.method == "POST":
        post = Post.objects.get(pk=post_pk)

        post.save()


