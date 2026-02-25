from django.urls import path
from . import views

urlpatterns = [
    path('dealers', views.get_dealers, name='get_dealers'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
]
