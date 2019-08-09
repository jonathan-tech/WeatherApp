from django.db import models

# Create your models here.
#alows to make city name table
class City(models.Model):
    name = models.CharField(max_length = 25)

    def __str__(self):
        return self.name
    #cities instead of city
    class Meta:
        verbose_name_plural = 'cities'
