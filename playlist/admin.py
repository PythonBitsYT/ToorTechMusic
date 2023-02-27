from django.contrib import admin
from playlist.models import Artist, Album, Track, Playlist, PlaylistTrack


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    """ Register Artist admin """
    list_display = ['id', 'name', 'gender', 'created_at', 'updated_at']
    search_fields = ['id', 'name']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """ Register Album admin """
    list_display = ['id', 'name', 'created_at', 'updated_at']
    search_fields = ['id', 'name']


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    """ Register Track admin """
    list_display = ['id', 'title', 'created_at', 'updated_at']
    search_fields = ['id', 'title']


class PlaylistTrackInline(admin.TabularInline):
    """ Playlist track inline """
    model = PlaylistTrack
    extra = 1


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    """ Register Playlist admin """
    inlines = (PlaylistTrackInline,)
    list_display = ['id', 'name', 'created_at', 'updated_at']
    search_fields = ['id', 'name', 'customer_id']
