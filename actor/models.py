from django.db import models
from django.urls import reverse

# actor app models.py

def upload_image(instance, filename):
    """Upload images function"""

    return f'images/{instance.first_name}_{instance.last_name}/{filename}'

class Actor(models.Model):
    """Actor model class"""

    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    description = models.TextField(null=True, blank=True)
    average_movie_rate = models.FloatField()
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to=upload_image, blank=True)


    def get_absolute_url(self):
        """Actor class meta class get absolute url function"""

        return reverse('actor:actor_detail', kwargs={'pk': self.pk})

    def __str__(self):
        """Actor class str function"""

        return f'{self.first_name} {self.last_name}'
    
    def movie_list(self):
        """Actor class movies function"""
        return ''.join([i.name for i in self.movies.all()])


    class Meta:
        """Actor class meta class"""

        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'
    
