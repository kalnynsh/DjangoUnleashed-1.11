from django.shortcuts import render

from .models import Post


def post_list(request):
    post_list_obj = Post.objects.all()
    template = 'blog/post_list.html'
    context = {'post_list': post_list_obj}

    return render(
        request,
        template,
        context,
    )
