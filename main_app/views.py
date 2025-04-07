from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Movie, Actor, Review
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReviewForm


class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movie-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def movie_index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

@login_required
def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    actors_movie_doesnt_have = Actor.objects.exclude(id__in=movie.actors.all().values_list('id'))
    review_form = ReviewForm()
    return render(request, 'movies/detail.html', {
        'movie': movie, 'review_form': review_form, 'actors': actors_movie_doesnt_have
    })

@login_required
def add_review(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('movie-detail', movie_id=movie.id)
    else:
        form = ReviewForm()

    return render(request, 'movies/detail.html', {
        'movie': movie, 'review_form': form 
    })

@login_required
def associate_actor(request, movie_id, actor_id):
    Movie.objects.get(id=movie_id).actors.add(actor_id)
    return redirect('movie-detail', movie_id=movie_id)

@login_required
def remove_actor(request, movie_id, actor_id):
    Movie.objects.get(id=movie_id).actors.remove(actor_id)
    return redirect('movie-detail', movie_id=movie_id)

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['name', 'director', 'genre', 'description', 'year', 'poster_image']

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = ['name', 'director', 'genre', 'description', 'year', 'poster_image']

class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    success_url = '/movies/'

class ActorCreate(LoginRequiredMixin, CreateView):
    model = Actor
    fields = '__all__'

class ActorList(LoginRequiredMixin, ListView):
    model = Actor

class ActorDetail(LoginRequiredMixin, DetailView):
    model = Actor

class ActorUpdate(LoginRequiredMixin, UpdateView):
    model = Actor
    fields = ['name', 'biography', 'date_of_birth', 'photo']

class ActorDelete(LoginRequiredMixin, DeleteView):
    model = Actor
    success_url = '/actors/'