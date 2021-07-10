from django.urls import path, include
from . import views as nonUserViews

urlpatterns = [
    path('', nonUserViews.redirectHome),
    path('logout/', nonUserViews.logout, name = 'logout'),
    path('home/', nonUserViews.homeView, name = 'home-page'),
    path('items/', nonUserViews.itemsView, name = 'home-items-page'),
    path('stores/', nonUserViews.storesView, name = 'home-stores-page'),
    path('aboutus/', nonUserViews.aboutView, name = 'about-page'),
    path('profile/', nonUserViews.profileView, name = 'profile-page')
]