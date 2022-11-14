from django.db import models
from django.core.cache import cache


class Country(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("name",)


class City(models.Model):

    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.country.name}-{self.name}"

    class Meta:
        ordering = ("name",)


class University(models.Model):

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=50)
    img = models.ImageField()
    type = models.CharField(max_length=50)
    overviwe = models.TextField()
    create_year = models.DateField()
    number_all_students = models.IntegerField()
    number_international_students = models.IntegerField()
    url = models.URLField(max_length=200)
    rate = models.IntegerField()

    def save(self):
        cache.clear()
        return super().save()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("name",)
