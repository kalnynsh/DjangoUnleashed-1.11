from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import (CreateView, DeleteView,
                                  DetailView, UpdateView, View)
from django.core.paginator import (Paginator,
                                   EmptyPage, PageNotAnInteger)

from .forms import TagForm, StartupForm, NewsLinkForm
from .models import Tag, Startup, NewsLink


class NewsLinkCreateView(CreateView, View):
    form_class = NewsLinkForm
    model = NewsLink
    # Model allow derive the name of template
    # template_name = 'organizer/newslink_form.html'


class NewsLinkDeleteView(DeleteView):
    model = NewsLink

    def get_success_url(self):
        return self.object.startup.get_absolute_url()


class NewsLinkUpdateView(UpdateView):
    form_class = NewsLinkForm
    model = NewsLink
    template_name_suffix = '_form_update'


class StartupCreateView(CreateView, View):
    form_class = StartupForm
    model = Startup
    # Model allow derive the name of template
    # template_name = 'organizer/startup_form.html'


class StartupDeleteView(DeleteView):
    model = Startup
    success_url = reverse_lazy('organizer_startup_list')
    # Take from app._meta.app_label/model._mata.model_name+suffix
    # template_name = 'organizer/startup_confirm_delete.html'


class StartupDetailView(DetailView):
    model = Startup


class StartupListView(View):
    page_kwarg = 'page'
    paginate_by = 5  # 5 items per page
    template_name = 'organizer/startup_list.html'

    def get(self, request):
        startups = Startup.objects.all()
        paginator = Paginator(startups, self.paginate_by)
        page_number = request.GET.get(self.page_kwarg)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)  # First
        except EmptyPage:
            page = paginator.page(paginator.num_pages)  # Last
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.previous_page_number()
            )
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.next_page_number()
            )
        else:
            next_url = None
        context = {
            'is_paginated': page.has_other_pages(),
            'paginator': paginator,
            'next_page_url': next_url,
            'previous_page_url': prev_url,
            'startup_list': page,
        }

        return render(
            request,
            self.template_name,
            context
        )


class StartupUpdateView(UpdateView):
    form_class = StartupForm
    model = Startup
    template_name_suffix = '_form_update'


class TagCreateView(CreateView, View):
    form_class = TagForm
    model = Tag
    # Model allow derive the name of template
    # template_name = 'organizer/tag_form.html'


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('organizer_tag_list')
    #  # Take from app._meta.app_label/model._mata.model_name+suffix
    # template_name = 'organizer/tag_confirm_delete.html'


class TagDetailView(DetailView):
    model = Tag


class TagListView(View):
    template_name = 'organizer/tag_list.html'

    def get(self, request):
        tags = Tag.objects.all()
        context = {
            'tag_list': tags,
        }

        return render(
            request,
            self.template_name,
            context
        )


class TagPageListView(View):
    paginate_by = 5
    template_name = 'organizer/tag_list.html'

    def get(self, request, page_number):
        tags = Tag.objects.all()
        paginator = Paginator(tags, self.paginate_by)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        if page.has_previous():
            prev_url = reverse('organizer_tag_page',
                               args=(page.previous_page_number(), ))
        else:
            prev_url = None
        if page.has_next():
            next_url = reverse('organizer_tag_page',
                               args=(page.next_page_number(), ))
        else:
            next_url = None
        context = {
            'is_paginated': page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'tag_list': page,
        }

        return render(
            request, self.template_name, context
        )


class TagUpdateView(UpdateView):
    form_class = TagForm
    model = Tag
    template_name_suffix = '_form_update'
