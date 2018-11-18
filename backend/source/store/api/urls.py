from .views import StoreViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'store', StoreViewSet)

urlpatterns = router.urls
