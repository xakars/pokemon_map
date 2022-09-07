from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    Image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    Pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    Lat = models.FloatField()
    Lon = models.FloatField()
    Appeared_at = models.DateTimeField(null=True, blank=True)
    Disappeared_at = models.DateTimeField(null=True, blank=True)
    Level = models.IntegerField(null=True, blank=True)
    Health = models.IntegerField(null=True, blank=True)
    Strength = models.IntegerField(null=True, blank=True)
    Defence = models.IntegerField(null=True, blank=True)
    Stamina = models.IntegerField(null=True, blank=True)
