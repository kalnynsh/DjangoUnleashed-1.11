from django.shortcuts import get_object_or_404, render

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


def post_detail(request, year, month, slug):
    post_detail_obj = get_object_or_404(
        Post,
        pub__date__year=year,
        pub__date__month=month,
        slug__iexact=slug)
    template = 'blog/post_detail.html'
    context = {'post_detail': post_detail_obj}

    return render(
        request,
        template,
        context,
    )
