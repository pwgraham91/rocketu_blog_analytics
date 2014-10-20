from blog.models import Post, Tag


def latest_post(request):
    return {
        'latest_post': Post.objects.latest('created')
    }

def blog_tags(request):
    return {
        'tags': Tag.objects.all(),
        'posts': Post.objects.all(),
        'tag_count': Tag.objects.count(),
    }