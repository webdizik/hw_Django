from rest_framework.routers import DefaultRouter

from .views import AdvertisementViewSet

router = DefaultRouter()

# подключение `AdvertisementViewSet`
router.register('advertisements', AdvertisementViewSet)

urlpatterns = router.urls