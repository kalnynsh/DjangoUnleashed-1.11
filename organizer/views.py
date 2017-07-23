from django.shortcuts import get_object_or_404, render

from .models import Tag


def homepage(request):
    tag_list = Tag.objects.all()
    template = 'organizer/tag_list.html'
    context = {'tag_list': tag_list}

    return render(
        request,
        template,
        context
    )


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    template = 'organizer/tag_detail.html'
    context = {'tag': tag}

    return render(
        request,
        template,
        context
    )
