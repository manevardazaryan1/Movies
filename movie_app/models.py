from django.db import models
from django.urls import reverse
from actor.models import Actor

# movie app models.py

def upload_news_image(instance, filename):
    """Upload images function"""

    return f'images/{instance.name}/{filename}'


class Movie(models.Model):
    """Movie model class"""

    name = models.CharField(max_length=155)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField()
    rate = models.FloatField()
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=upload_news_image, blank=True)
    is_published = models.BooleanField(default=True)
    actors = models.ManyToManyField(Actor, related_name='movies')

    def __str__(self):
        """Movie class str function"""
        return self.name

    class Meta:
        """Movie class meta class"""

        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def get_absolute_url(self):
        """Movie class meta class get absolute url function"""

        return reverse('movie:detail', kwargs={'pk': self.pk})


