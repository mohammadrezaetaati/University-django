from django.urls import path
from django.views.decorators.cache import cache_page

from university.views import DetailUniversity, UniversityViwe


urlpatterns = [
    path("", cache_page(60 * 2)(UniversityViwe.as_view()), name="list-university"),
    path(
        "<int:id>",
        cache_page(60 * 2)(DetailUniversity.as_view()),
        name="detail-university",
    ),
]
