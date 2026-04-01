from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Genre, Tracks, Artist
from .forms import GenreForm, TrackForm, ArtistForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def genres(request):
    genre = Genre.objects.all()
    return render(request, 'genres.html', {'genres': genre})

def tracks(request):
    track = Tracks.objects.all()
    a = Artist.objects.all()
    artist = None
    if request.method == "POST":
        id_artist = request.POST.get('artist')
        artist = Artist.objects.get(id=id_artist)
        track = Tracks.objects.filter(artist=artist)
        
    return render(request, 'track.html', {'tracks': track, 'artists': a, 'current_artist': artist})

def addArtists(request):
    if request.method == "POST":
        artists = ArtistForm(request.POST, request.FILES)
        if artists.is_valid():
            artists.save()
            print("OK")
        else:
            print("(((")
        return redirect('/artists')
    else:
        addFormArtists = ArtistForm()
        return render(request, "add_artists.html", {"form": addFormArtists})
    
def artists(request):
    a = Artist.objects.all()
    return render(request, 'artists.html', {'artists': a})

def deleteGenres(request, id_genre):
    genre = Genre.objects.get(id=id_genre)
    genre.delete()
    return HttpResponse('<h1>Жанр успешно удален</h1><br><a href="/">На главную</a>')

def addGenres(request):
    if request.method == "POST":
        genre = GenreForm(request.POST)
        if genre.is_valid():
            genre.save()
        return redirect('/genres')
    else:
        addFormGenres = GenreForm()
        return render(request, "add_genres.html", {"form": addFormGenres})

def editGenre(request, id_genre):
    genre = Genre.objects.get(id=id_genre)
    if request.method == "POST":
        genre = GenreForm(request.POST, instance=genre)
        if genre.is_valid():
            genre.save()
        return redirect("/genres")
    else:
        genreform = GenreForm(instance=genre)
        return render(request, "add_genres.html", {"form": genreform})

def deleteTrack(request, id_track):
    track = Tracks.objects.get(id=id_track)
    track.delete()
    return HttpResponse('<h1>Трэк успешно удален</h1><br><a href="/">На главную</a>')

def addTrack(request):
    if request.method == "POST":
        track = TrackForm(request.POST)
        if track.is_valid():
            track.save()
        return redirect('/tracks')
    else:
        addFormTracks = TrackForm()
        return render(request, "add_track.html", {"form": addFormTracks})

def editTrack(request, id_track):
    track = Tracks.objects.get(id=id_track)
    if request.method == "POST":
        track = TrackForm(request.POST, instance=track)
        if track.is_valid():
            track.save()
        return redirect("/tracks")
    else:
        trackform = TrackForm(instance=track)
        return render(request, "add_track.html", {"form": trackform})
    

    

# #форма для редактирования 
# def formEditGenre(request, id_genre):
#     genre = Genre.objects.get(id=id_genre)
#     return render(request, 'editGenre.html', {'old': genre, 'id': id_genre})

# #редактирование 
# def editGenre(request):
#     id = request.POST.get("id")
#     name_en = request.POST.get("name_en")
#     name_ru = request.POST.get("name_ru")
#     description = request.POST.get("desc")
#     genres = Genre.objects.get(id=id)
#     genres.name_en = name_en
#     genres.name_ru = name_ru
#     genres.description = description
    
#     genres.save()
#     return HttpResponseRedirect("/editgenreform/"+id)
