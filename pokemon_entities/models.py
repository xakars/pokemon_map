from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    Image = models.ImageField(null=True)

    def __str__(self):
        return self.title