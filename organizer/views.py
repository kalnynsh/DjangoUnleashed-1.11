from django.http.response import Http404, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render_to_response

from .models import Tag


def homepage(request):

    return render_to_response(
        'organizer/tag_list.html',
        {'tag_list': Tag.objects.all()}
    )


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    template = loader.get_template('organizer/tag_detail.html')
    context = {'tag': tag}

    return HttpResponse(template.render(context))
