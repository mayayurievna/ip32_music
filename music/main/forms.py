from django import forms
from .models import Genre
from .models import Tracks
from .models import Artist

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name_en', 'name_ru', 'description']
        labels = {
            'name_en': 'Название на английском',
            'name_ru': 'Название на русском',
            'description': 'Описание',
        }
     
class TrackForm(forms.ModelForm):
    class Meta:
        model = Tracks
        fields = ['title', 'duration', 'genre']
        labels = {
            'title': 'Название песни',
            'duration': 'Длительность песни',
            'genre': 'Жанры',
        }


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        labels = {
            'name': 'Имя / название',
            'image': 'Фотография',
        }