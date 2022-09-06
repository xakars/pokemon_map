from django.db import models  # noqa F401

class Pokemons(models.Model):
    title = models.CharField(max_length=200)