from django.urls import path
from . import views

urlpatterns = [
    path('dealers', views.get_dealers, name='get_dealers'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('fetchReviews/dealer/<int:dealer_id>', views.fetch_reviews, name='fetch_reviews'),
    path('fetchDealers', views.fetch_dealers, name='fetch_dealers'),
    path('fetchDealer/<int:dealer_id>', views.fetch_dealer_by_id, name='fetch_dealer_by_id'),
    path('fetchDealers/<str:state>', views.fetch_dealers_by_state, name='fetch_dealers_by_state'),
]
