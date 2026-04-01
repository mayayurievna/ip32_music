from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('genres/', views.genres),
    path('track/', views.tracks),
    path('deletegenre/<int:id_genre>', views.deleteGenres),
    path('addgenre/', views.addGenres),
    path('editgenre/<int:id_genre>', views.editGenre),

    path('deletetrack/<int:id_track>', views.deleteTrack),
    path('addtrack/', views.addTrack),
    path('edittrack/<int:id_track>', views.editTrack),
    
    path('artists/', views.artists),

    path('artists/', views.addArtists),
    path('addartist/', views.addArtists),
]
