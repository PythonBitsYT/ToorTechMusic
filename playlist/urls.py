from rest_framework import routers
from playlist.views import PlayListViewSet, ArtistViewSet, AlbumViewSet, TrackViewSet



router = routers.SimpleRouter()
router.register(r'playlist', PlayListViewSet)
router.register(r'artist', ArtistViewSet)
router.register(r'album', AlbumViewSet)
router.register(r'track', TrackViewSet)
urlpatterns = router.urls
