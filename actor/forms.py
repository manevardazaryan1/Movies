from django import forms
from .models import Actor
from django.db.models import Min, Max

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name',
                  'description', 'average_movie_rate',
                  'date_of_birth', 'image']


class ActorSearchForm(forms.Form):
    first_name= forms.CharField(required=False)
    first_name= forms.CharField(required=False)

    average_movie_rate_from = forms.ChoiceField(choices=[(i, i) for i in range(1, 11)], required=False)
    search = forms.CharField(initial='True', widget=forms.HiddenInput())
