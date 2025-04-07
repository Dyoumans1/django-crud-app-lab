from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    
    path('movies/', views.movie_index, name='movie-index'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie-detail'),
    path('movies/create/', views.MovieCreate.as_view(), name='movie-create'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movie-update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movie-delete'),
    
    path('movies/<int:movie_id>/add_review/', views.add_review, name='add-review'),
    
    path('actors/', views.ActorList.as_view(), name='actor-list'),
    path('actors/<int:pk>/', views.ActorDetail.as_view(), name='actor-detail'),
    path('actors/create/', views.ActorCreate.as_view(), name='actor-create'),
    path('actors/<int:pk>/update/', views.ActorUpdate.as_view(), name='actor-update'),
    path('actors/<int:pk>/delete/', views.ActorDelete.as_view(), name='actor-delete'),
    
    path('movies/<int:movie_id>/associate_actor/<int:actor_id>/', views.associate_actor, name='associate-actor'),
    path('movies/<int:movie_id>/remove_actor/<int:actor_id>/', views.remove_actor, name='remove-actor'),
]
