from rest_framework import routers
from .viewsets import HorizonViewSet

router = routers.SimpleRouter()
router.register('horizon', HorizonViewSet)


urlpatterns = router.urls 