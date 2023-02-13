from movie_app import views
from django.urls import path

# movie app urls file

app_name = 'movie'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('movie/detail/<int:pk>/', views.detail_view, name='detail'),
    path('movie/add-movie/', views.AddMovie.as_view(), name='add_movie'),
    path('movie/update/<int:pk>/', views.UpdateMovie.as_view(), name='update'),
    path('movie/delete/<int:pk>/', views.MovieDeleteView.as_view(), name='delete'),
]
