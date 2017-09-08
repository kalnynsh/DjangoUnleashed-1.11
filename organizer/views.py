from django.shortcuts import get_object_or_404, render, redirect

from .models import Tag, Startup
from .forms import TagForm


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


def tag_list(request):
    template = 'organizer/tag_list.html'
    context = {'tag_list': Tag.objects.all()}

    return render(
        request,
        template,
        context
    )


def tag_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TagForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_tag = form.save()
            # Return new URL
            # tag_url = new_tag.get_absolute_url()
            #  HttpResponseRedirect(tag_url)
            return redirect(new_tag)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TagForm()

    template = 'organizer/tag_form.html'
    context = {'form': form}

    return render(request, template, context)


def startup_list(request):
    startup_list_obj = Startup.objects.all()
    template = 'organizer/startup_list.html'
    context = {'startup_list': startup_list_obj}

    return render(
        request,
        template,
        context
    )


def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    template = 'organizer/startup_detail.html'
    context = {'startup': startup}

    return render(
        request,
        template,
        context
    )
