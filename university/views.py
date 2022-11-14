
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import Count

from .models import City, Country, University
from .forms import UniversityForm


class UniversityViwe(ListView):

    model = University
    template_name = "list-university.html"
    context_object_name = "universities"
    form_class = UniversityForm
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["country"] = Country.objects.all().order_by('name')
        context["city"] = City.objects.values("name").annotate(Count("name")).order_by('name')
        context["get_country"] = self.request.GET.getlist("country")
        context["get_city"] = self.request.GET.getlist("city")
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        form = self.form_class(self.request.GET)
        if form.is_valid():
            search = form.cleaned_data.get("search")
            city = form.cleaned_data.get("city")
            country = form.cleaned_data.get("country")
            if country and city:
                qs = (
                    super()
                    .get_queryset()
                    .filter(city_id__in=city, city__country_id__in=country)
                )
            elif country:
                qs = super().get_queryset().filter(city__country_id__in=country)
            elif city:
                qs = super().get_queryset().filter(city_id__in=city)
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
