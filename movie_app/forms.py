from django import forms
from .models import Movie
from actor.models import Actor
from django.db.models import Min, Max

# movie app form.py

class MovieForm(forms.ModelForm):
    """Movie form class"""

    class Meta:
        """Movie form meta class"""
        
        model = Movie
        fields = ['name', 'description',
                  'duration', 'rate',
                  'year', 'image', 'actors']

    actors = forms.ModelMultipleChoiceField(
        queryset=Actor.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class MovieSearchForm(forms.Form):
    """Movie search form class"""

    name = forms.CharField(required=False)
    year_from = forms.ChoiceField(choices=[(None, '---'),
                                           *[(i, i) for i in range(Movie.objects.aggregate(Min('year'))['year__min'],
                                                                   Movie.objects.aggregate(Max('year'))[
                                                                       'year__max'] + 1)]
                                           ], required=False)
    year_to = forms.ChoiceField(choices=[(None, '---'),
                                         *[(i, i) for i in range(Movie.objects.aggregate(Min('year'))['year__min'],
                                                                 Movie.objects.aggregate(Max('year'))[
                                                                     'year__max'] + 1)],

                                         ], required=False)
    rate_from = forms.ChoiceField(choices=[(i, i) for i in range(1, 11)], required=False)
    search = forms.CharField(initial='True', widget=forms.HiddenInput())
