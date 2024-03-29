from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page),
    path('register', views.register),
    path('login', views.login),
    path('theWall', views.theWall),
    path('theWall/post_message', views.post_message),
    path('theWall/post_comment', views.post_comment),
    path('logout', views.logout),
]