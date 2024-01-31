from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('get_map_tile/<int:z>/<int:x>/<int:y>/', views.get_map_tile, name='get_map_tile'),

]
