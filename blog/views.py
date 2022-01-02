from django.shortcuts import render
from . import models


# Create your views here.
def get_post(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post': post})


def post_detail(request, id):
    try:
        post = models.Post.objects.get(id=id)
    except models.Post.DoesNotExist:
        raise Http404('Post does not exist, Billarder')

    return render(request, 'post_detail.html', {'post': post})
