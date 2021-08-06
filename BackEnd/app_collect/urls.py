from rest_framework.routers import SimpleRouter

from app_collect.views import EquipmentsInfoViewSet

router = SimpleRouter()
router.register(r'EquipmentsInfo', EquipmentsInfoViewSet, 'EquipmentsInfo')

urlpatterns = router.urls
