from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, View)
from django.core.paginator import (Paginator,
                                   EmptyPage, PageNotAnInteger)

from .forms import TagForm, StartupForm, NewsLinkForm
from .models import Tag, Startup, NewsLink
from core.utils import UpdateView
from .utils import PageLinksMixin


class NewsLinkCreateView(CreateView):
    form_class = NewsLinkForm
    model = NewsLink


class NewsLinkDeleteView(DeleteView):
    model = NewsLink

    def get_success_url(self):
        return self.object.startup.get_absolute_url()


class NewsLinkUpdateView(UpdateView):
    form_class = NewsLinkForm
    model = NewsLink


class StartupCreateView(CreateView):
    form_class = StartupForm
    model = Startup


class StartupDeleteView(DeleteView):
    model = Startup
    success_url = reverse_lazy('organizer_startup_list')
    # Take from app._meta.app_label/model._mata.model_name+suffix
    # template_name = 'organizer/startup_confirm_delete.html'


class StartupDetailView(DetailView):
    model = Startup


class StartupListView(PageLinksMixin, ListView):
    model = Startup
    paginate_by = 5  # 5 items per page


class StartupUpdateView(UpdateView):
    form_class = StartupForm
    model = Startup


class TagCreateView(CreateView, View):
    form_class = TagForm
    model = Tag


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('organizer_tag_list')


class TagDetailView(DetailView):
    model = Tag


class TagListView(PageLinksMixin, ListView):
    model = Tag
    paginate_by = 5


class TagUpdateView(UpdateView):
    form_class = TagForm
    model = Tag
