from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View

from .models import Tag, Startup, NewsLink
from .forms import TagForm, StartupForm, NewsLinkForm
from .utils import ObjectCreateMixin


class NewsLinkCreateView(ObjectCreateMixin, View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form.html'


class NewsLinkUpdateView(View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form_update.html'

    def get(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        context = {'form': self.form_class(instance=newslink),
                   'newslink': newslink, }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        bound_form = self.form_class(request.POST, instance=newslink)
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink)
        else:
            context = {
                'form': bound_form,
                'newslink': newslink,
            }
            return render(request, self.template_name, context)


class StartupCreateView(ObjectCreateMixin, View):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'


def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    template = 'organizer/startup_detail.html'
    context = {'startup': startup}

    return render(
        request,
        template,
        context
    )


def startup_list(request):
    startup_list_obj = Startup.objects.all()
    template = 'organizer/startup_list.html'
    context = {'startup_list': startup_list_obj}

    return render(
        request,
        template,
        context
    )


class TagCreateView(ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    template = 'organizer/tag_detail.html'
    context = {'tag': tag}

    return render(
        request,
        template,
        context
    )


def tag_list(request):
    template = 'organizer/tag_list.html'
    context = {'tag_list': Tag.objects.all()}

    return render(
        request,
        template,
        context
    )
