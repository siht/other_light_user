from rest_framework import routers
from .views import UserViewSet
__all__ = ('router',)


router = routers.DefaultRouter()
router.register('users', UserViewSet)
