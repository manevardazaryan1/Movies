from django.shortcuts import render, get_object_or_404
from actor.models import Actor
from actor.forms import ActorForm, ActorSearchForm
from django.db.models import Q
from django.views.generic import (ListView,UpdateView, CreateView, DeleteView)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# actor app view.py

class LoginRequiredMixin:
    """Login required mixin class"""

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        """Login required dispatch mixin"""

        return super().dispatch(request, *args, **kwargs)

class ActorView(ListView):
    """Actors view class"""

    model = Actor
    template_name = '../templates/actor/index.html'
    queryset = Actor.objects.all().order_by('-pk')
    paginate_by = 12
    context_object_name = 'actor'
    form_class = ActorSearchForm

    def get_queryset(self):
        """ActorView class get queryset function"""

        if self.request.GET.get('search'):
            first_name = Q(first_name__icontains=self.request.GET.get('first_name', ''))
            last_name = Q(last_name__icontains=self.request.GET.get('last_name', ''))
            average_movie_rate_from = Q(average_movie_rate__gte=self.request.GET.get('average_movie_rate_from', 0))
            self.queryset = self.queryset.filter(first_name, last_name,average_movie_rate_from)
            
        return self.queryset 

    def get_context_data(self, **kwargs):
        """ActorView class get context data function"""

        context = super(ActorView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        return context


def actor_detail_view(request, pk):
    """Actor detail class"""

    actor = get_object_or_404(Actor, pk=pk)
    rate = range(int(actor.average_movie_rate))
    return render(request, '../templates/actor/detail.html', {'actor': actor, 'rate':rate})


class AddActor(LoginRequiredMixin,CreateView):
    """Add actor class"""

    model = Actor
    form_class = ActorForm
    template_name = 'actor/add_actor.html'


class UpdateActor(LoginRequiredMixin,UpdateView):
    """Update actor class"""

    model = Actor
    form_class = ActorForm
    template_name = 'actor/update_actor.html'


class ActorDeleteView(DeleteView):
	"""Delete movie class"""

	model =  Actor
	success_url = '/actors'
	template_name = 'actor/delete_actor.html'
	queryset = Actor.objects.all()