import datetime
from django.db.models import Q
from movie_app.models import Movie
from .forms import MovieForm, MovieSearchForm
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView, UpdateView, CreateView, DeleteView)


# movie app views.py


class LoginRequiredMixin:
    """Login required mixin class"""

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        """Login required dispatch mixin"""

        return super().dispatch(request, *args, **kwargs)


class IndexView(ListView):
    """Movies view class"""

    model = Movie
    template_name = '../templates/movie_app/index.html'
    queryset = Movie.objects.all().order_by('-pk')
    paginate_by = 12
    context_object_name = 'movie'
    form_class = MovieSearchForm

    def get_queryset(self):
        """IndexView class get queryset function"""

        if self.request.GET.get('search'):
            name = Q(name__icontains=self.request.GET.get('name', ''))
            year_from = self.request.GET.get('year_from', 0)
            if year_from == '':
                year_from = 0
            year_from = Q(year__gte=year_from)
            year_to = self.request.GET.get('year_to', datetime.date.today().year)
            if year_to == '':
                year_to = datetime.date.today().year
            year_to = Q(year__lte=year_to)
            rate_from = Q(rate__gte=self.request.GET.get('rate_from', 0))
            self.queryset  = self.queryset.filter(name, year_from, year_to, rate_from)
        
        return self.queryset 

    def get_context_data(self, **kwargs):
        """IndexView class get context data function"""

        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        return context


def detail_view(request, pk):
    """Movies detail class"""

    movie = get_object_or_404(Movie, pk=pk)
    rate = range(int(movie.rate))
    return render(request, '../templates/movie_app/detail.html', {'movie': movie, 'rate': rate})

class AddMovie(LoginRequiredMixin,CreateView):
    """Add movie class"""

    model = Movie
    form_class = MovieForm
    template_name = 'movie_app/add_movie.html'

    def get_context_data(self, **kwargs):
        """AddMovie class get context data function"""

        context = super(AddMovie, self).get_context_data(**kwargs)
        context = {'form': self.form_class,'add_actor': True}
        return context

class UpdateMovie(LoginRequiredMixin,UpdateView):
    """Update movie class"""

    model = Movie
    form_class = MovieForm
    template_name = 'movie_app/update_movie.html'

    def get_context_data(self, **kwargs):
        """UpdateMovie class get context data function"""

        context = super(UpdateMovie, self).get_context_data(**kwargs)
        movie = get_object_or_404(self.model, pk=self.kwargs['pk'])
        context = {'form': self.form_class(instance=movie),'add_actor': True, 'movie_id': self.kwargs['pk']}
        return context

class MovieDeleteView(DeleteView):
	"""Delete movie class"""

	model =  Movie
	success_url = '/'
	template_name = 'movie_app/delete_movie.html'
	queryset = Movie.objects.all()