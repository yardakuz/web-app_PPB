from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

class Street(models.Model):
    name = models.CharField('Название', max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField('Название', max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    home = models.IntegerField('Дом')
    time_open = models.TimeField('Время открытия')
    time_close = models.TimeField('Время закрытия')

    def __str__(self):
        return self.name
