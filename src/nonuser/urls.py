from django.urls import path, include
from . import views as nonUserViews

urlpatterns = [
    path('items/', nonUserViews.itemsView, name = 'home-items-page'),
    path('stores/', nonUserViews.storesView, name = 'home-stores-page'),
    path('aboutus/', nonUserViews.aboutView, name = 'about-page'),
]