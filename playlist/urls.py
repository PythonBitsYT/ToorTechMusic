from rest_framework import routers
from playlist.views import PlayListViewSet



router = routers.SimpleRouter()
router.register(r'playlist', PlayListViewSet)
urlpatterns = router.urls