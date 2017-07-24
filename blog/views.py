from django.views.generic import View
from django.shortcuts import get_object_or_404, render

from .models import Post


class PostListView(View):
    template_name = 'blog/post_list.html'

    def get(self, request, parent_template=None):
        post_list_obj = Post.objects.all()
        context = {'post_list': post_list_obj,
                   'parent_template': parent_template, }

        return render(
            request,
            self.template_name,
            context
        )


def post_detail(request, year, month, slug, parent_template=None):
    post_detail_obj = get_object_or_404(
        Post,
        pub__date__year=year,
        pub__date__month=month,
        slug__iexact=slug)
    template = 'blog/post_detail.html'
    context = {'post': post_detail_obj, 'parent_template': parent_template, }

    return render(
        request,
        template,
        context,
    )
