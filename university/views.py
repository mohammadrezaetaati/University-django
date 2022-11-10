from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import University


class UniversityViwe(ListView):

    model = University
    template_name = "list-university.html"
    context_object_name = "universities"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        filter_country = self.request.GET.get("filter_country")
        filter_city = self.request.GET.get("filter_city")
        search = self.request.GET.get("search")
        if filter_country:
            qs = super().get_queryset().filter(city__country__name=filter_country)
        elif filter_city:
            qs = super().get_queryset().filter(city__name=filter_city)
        elif search:
            qs = (
                super()
                .get_queryset()
                .filter(
                    Q(name__contains=search)
                    | Q(city__name__contains=search)
                    | Q(city__country__name__contains=search)
                )
            )
        return qs


class DetailUniversity(DetailView):

    model = University
    template_name = "detail.html"
    pk_url_kwarg = "id"
    context_object_name = "university"
