from localflavor.us.us_states import STATES_NORMALIZED
from blog.models import Post, Tag, Ad


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

def serve_ads(request):
    user_state = request.location['region'].lower()
    location = STATES_NORMALIZED[user_state]
    available_ad = Ad.objects.filter(state=location).order_by('?')[:1]
    return {
        'available_ad': available_ad
    }