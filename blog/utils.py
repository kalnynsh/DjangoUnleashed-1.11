from django.shortcuts import get_object_or_404

from .models import Post


class PostGetMixin:
    month_url_kwarg = 'month'
    year_url_kwarg = 'year'
    slug_url_kwarg = 'slug'

    errors = {
        'url_kwargs':
            "Generic view {} must be called with "
            "year, month, slug."

    }

    def get_object(self, queryset=None):
        year = self.kwargs.get(self.month_url_kwarg)
        month = self.kwagrs.get(self.year_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if (year is None
                or month is None
                or slug is None):
            raise AttributeError(
                self.errors['url_kwargs'].format(self.__class__.__name__)
            )

        return get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug__iexact=slug
        )
