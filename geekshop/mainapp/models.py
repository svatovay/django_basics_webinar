from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='название категории', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return f'{self.id}. {self.name}'
