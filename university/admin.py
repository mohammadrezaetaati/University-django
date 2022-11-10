from django.contrib import admin

from .models import City, Country, University


admin.site.register(City)
admin.site.register(Country)


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    def city_name(self, obj):
        return obj.city.name

    def country_name(self, obj):
        return obj.city.country.name

    list_display = ("name", "city_name", "country_name")
