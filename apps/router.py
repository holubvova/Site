from rest_framework import routers

from apps.serializers import ProductViewSet, OrderViewSet, OrderItemViewSet, ShippingAddressViewSet
from apps.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitems', OrderItemViewSet)
router.register(r'shippingaddress', ShippingAddressViewSet)
