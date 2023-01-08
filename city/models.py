from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название города')
    country = models.ForeignKey('city.Country', on_delete=models.CASCADE, verbose_name='Страна')

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ['name']

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название страны')

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
        ordering = ['name']

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название улицы')
    city = models.ForeignKey('city.City', on_delete=models.CASCADE, verbose_name='Город')

    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"
        ordering = ['name']

    def __str__(self):
        return self.name
