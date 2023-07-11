from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movies),
    # path('movie/<int:id_movie>', views.show_one_movie, name="movie_info"),
    path('movie/<slug:slug_movie>', views.show_one_movie, name="movie_info"),
    path('directors/', views.show_all_directors),
    path('directors/<int:id_direct>', views.show_one_director, name="direct_info"),
    # path('directors/<slug:slug_direct>', views.show_one_director, name="direct_info"),
    path('actors/', views.show_all_actors),
    path('actors/<int:id_actor>', views.show_one_actor, name="actor_info"),
]
