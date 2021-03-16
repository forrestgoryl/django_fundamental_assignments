from django.urls import path
from . import views
urlpatterns = [
    path('', views.shows),
    path('shows', views.shows),
    path('shows/', views.shows),
    path(f'shows/<int:show_number>', views.shows_id),
    path(f'shows/<int:show_number>/', views.shows_id),
    path(f'shows/<int:show_number>/edit', views.shows_edit),
    path(f'shows/<int:show_number>/edit/', views.shows_edit),
    path(f'shows/<int:show_number>/update', views.update),
    path(f'shows/<int:show_number>/update/', views.update),
    path(f'shows/<int:show_number>/delete', views.delete),
    path(f'shows/<int:show_number>/delete/', views.delete),
    path('shows/new', views.shows_new),
    path('shows/new/', views.shows_new),
    path('shows/create', views.shows_create),
    path('shows/create/', views.shows_create),
]