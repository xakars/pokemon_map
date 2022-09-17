from django.db import models  # noqa F401

class Pokemon(models.Model):
    """Покемон"""
    title = models.CharField('Название покемона',max_length=200)
    image = models.ImageField('Изображение покемона', null=True)
    description = models.TextField('Описание покемона', blank=True)
    title_en = models.CharField('Название покемона на англ.', blank=True, max_length=200)
    title_jp = models.CharField('Название покемона на япон.', blank=True, max_length=200)
    previous_evolution = models.ForeignKey('self',
                                           null=True,
                                           verbose_name='Из кого эволюционирует',
                                           blank=True,
                                           related_name='next_evolutions',
                                           on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    """Данные о покемоне"""
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE,
                                verbose_name='Покемон',
                                related_name = 'entities')
    lat = models.FloatField('Широта', blank=True)
    lon = models.FloatField('Долгота', blank=True)
    appeared_at = models.DateTimeField('Дата и Время появления', null=True, blank=True)
    disappeared_at = models.DateTimeField('Дата и Время исчезновения', null=True, blank=True)
    level = models.IntegerField('Уровень', null=True, blank=True)
    health = models.IntegerField('Здоровье', null=True, blank=True)
    strength = models.IntegerField('Сила', null=True, blank=True)
    defence = models.IntegerField('Защита', null=True, blank=True)
    stamina = models.IntegerField('Выносливость', null=True, blank=True)
