from rest_framework import routers
from customers.views import CustomerViewSet



router = routers.SimpleRouter()
router.register(r'customer', CustomerViewSet)
urlpatterns = router.urls