from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    category = models.CharField(max_length=200, verbose_name="Категория")
    quantity = models.IntegerField(verbose_name="Количество")
    description = models.TextField(verbose_name="Описание")

