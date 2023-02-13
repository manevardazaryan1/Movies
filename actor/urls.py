from actor import views
from django.urls import path

# actor app urls.py

app_name = 'actor' 

urlpatterns = [
    path('actors/', views.ActorView.as_view(), name='actors'),
    path('actor/detail/<int:pk>/', views.actor_detail_view, name='actor_detail'),
    path('actor/add-actor/', views.AddActor.as_view(), name='add_actor'),
    path('actor/update/<int:pk>/', views.UpdateActor.as_view(), name='update'),
    path('actor/delete/<int:pk>/', views.ActorDeleteView.as_view(), name='delete'),
]
