from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods
from django.views.generic import View

from .models import Post
from .forms import PostForm


class PostCreateView(View):
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            return render(request, self.template_name, {'form': bound_form})


@require_http_methods(['HEAD', 'GET'])
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
