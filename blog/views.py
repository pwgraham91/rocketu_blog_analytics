from django.shortcuts import render, get_object_or_404
from blog.models import Post, Tag


def blog(request):
    return render(request, 'blog.html', {
        'posts': Post.objects.order_by('-created')
    })


def post(request, pk):
    post_obj = get_object_or_404(Post, pk=pk)

    return render(request, 'post.html', {
        'post': post_obj
    })


def blog_list(request, pk):
    posts_specific = Post.objects.filter(tags__pk=pk)
    tag = Tag.objects.get(pk=pk)
    data = {
        'posts_specific': posts_specific,
        'tag': tag
    }
    return render(request, 'blog_list.html', data)