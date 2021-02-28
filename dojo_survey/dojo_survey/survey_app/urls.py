from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('result', views.result),
    path('wipe', views.wipe),
]