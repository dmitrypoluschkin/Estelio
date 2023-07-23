from django.db import models


class Cities(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    long = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Долгота")
    lat = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Широта")

    # stores = models.CharField(max_length=255, verbose_name="Магазин")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Города"
        verbose_name_plural = "Города"
        ordering = ['title']


class Stores(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    long = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Долгота")
    lat = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Широта")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    email = models.EmailField(max_length=254, null=True, verbose_name="E-mail")
    website = models.URLField(max_length=200, verbose_name="Сайт")
    city = models.ForeignKey('Cities', on_delete=models.CASCADE,
                             null=True, verbose_name="Город")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Магазины"
        verbose_name_plural = "Магазины"
        ordering = ['title', 'city']
