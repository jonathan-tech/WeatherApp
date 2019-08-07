from django.db import models

# Create your models here.
#alows to make city name table
class City(models.Model):
    name = models.CharField(max_length = 25)

    def __str__(self):
        return self.name
    #city ies instead of s
    class Meta:
        verbose_name_plural = 'cities'
