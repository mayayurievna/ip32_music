from django.contrib import admin
from .models import Genre, Tracks,Artist

# Register your models here.
admin.site.register(Genre)
admin.site.register(Tracks)
admin.site.register(Artist)