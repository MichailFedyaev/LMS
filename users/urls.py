from rest_framework.routers import SimpleRouter

from .views import CustomUserViewSet, PaymentViewSet

app_name = 'users'

router_user = SimpleRouter()
router_payment = SimpleRouter()

router_user.register('user', CustomUserViewSet)
router_payment.register('payment', CustomUserViewSet)

urlpatterns = router_user.urls + router_payment.urls
