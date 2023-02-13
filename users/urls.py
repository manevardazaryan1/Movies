from users import views
from django.urls import path

# user app urls.py

app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/<str:user_name>', views.profile, name='profile'),
    path('update_profile/<str:user_name>', views.UpdateUserView.as_view(), name='update_profile'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
