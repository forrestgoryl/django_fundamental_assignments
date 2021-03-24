from django.urls import path
from . import views
urlpatterns = [
    path('', views.landingpage),
    path('homepage', views.homepage),
    path('register', views.register),
    path('login', views.login),
    path('add_book', views.add_book),
    path('edit_book', views.edit_book),
    path('edit', views.edit),
    path('delete', views.delete),
    path('view_book/<int:id>', views.book),
    path('favorite_book', views.favorite_book),
    path('unfavorite', views.unfavorite),
    path('logout', views.logout),
]