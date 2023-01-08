from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название магазина')
    city = models.ForeignKey('city.City', on_delete=models.CASCADE, verbose_name='Город')
    street = models.ForeignKey('city.Street', on_delete=models.CASCADE, verbose_name='Улица')
    house = models.CharField(max_length=255, verbose_name='Дом')
    open_at = models.TimeField(verbose_name='Время открытия')
    close_at = models.TimeField(verbose_name='Время закрытия')

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
        ordering = ['name']

    def __str__(self):
        return self.name
