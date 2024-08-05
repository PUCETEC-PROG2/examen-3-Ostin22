# Ingresar tus URLs de la app aquí

from django.urls import path

from . import views

app_name = 'discos'

urlpatterns = [
    path("", views.index, name="index"),
    path("add_artist/", views.add_artist, name="add_artist"),
    path("artist/", views.artist_list, name="artist_list"),
    path("artist/artist/<int:artist_id>", views.artist, name="artist_id"),
    path("artist/edit_artist/<int:id>", views.edit_artist, name="edit_artist"),
    path("artist/delete_artist/<int:id>", views.delete_artist, name="delete_artist"),
    path("disco/<int:disco_id>/", views.disco, name="disco_id"),
    path("add_disco/", views.add_disco, name="add_disco"),
    path("edit_disco/<int:id>", views.edit_disco, name="edit_disco"),
    path("delete_disco/<int:id>", views.delete_disco, name="delete_disco")

    
    
]
