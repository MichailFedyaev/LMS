from rest_framework.routers import SimpleRouter

from .views import CustomUserViewSet

app_name = 'users'

router = SimpleRouter()
router.register('', CustomUserViewSet)
urlpatterns = router.urls
