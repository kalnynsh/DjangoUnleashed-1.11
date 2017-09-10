from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View

from .models import Tag, Startup
from .forms import TagForm, StartupForm, NewsLinkForm


class NewsLinkCreateView(View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink)
        else:
            return render(request, self.template_name, {'form': bound_form})


class StartupCreateView(View):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_startup = bound_form.save()
            return redirect(new_startup)
        else:
            return render(request, self.template_name, {'form': bound_form})


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


class TagCreateView(View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'

    def get(self, request):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        else:
            return render(request, self.template_name, {'form': bound_form})


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
