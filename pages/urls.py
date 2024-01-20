from django.urls import path
from .views import HomePageView,ProfilePageView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('logout_user', views.logout_user, name='logout')
]
