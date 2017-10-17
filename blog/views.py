from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import (ArchiveIndexView, CreateView, DetailView,
                                  MonthArchiveView, View, YearArchiveView,
                                  UpdateView)

from .models import Post
from .forms import PostForm
from .utils import PostGetMixin


class PostArchiveMonthView(MonthArchiveView):
    model = Post
    date_field = 'pub_date'
    month_format = '%m'


class PostArchiveYearView(YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True


class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    # template_name = 'blog/post_form.html' derive from model name


class PostDeleteView(View):
    def get(self, request, year, month, slug):
        post = get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug__iexact=slug
        )
        return render(request,
                      'blog/post_confirm_delete.html',
                      {'post': post})

    def post(self, request, year, month, slug):
        post = get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug__iexact=slug
        )
        post.delete()
        return redirect('blog_post_list')


class PostDetailView(PostGetMixin, DetailView):
    model = Post


class PostListView(ArchiveIndexView):
    allow_empty = True
    allow_future = True
    context_object_name = 'post_list'
    date_field = 'pub_date'
    make_object_list = True
    model = Post
    paginate_by = 3
    template_name = 'blog/post_list.html'


class PostUpdateView(PostGetMixin, UpdateView):
    form_class = PostForm
    model = Post
