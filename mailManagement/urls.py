from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from mailManagement.views import *


router = DefaultRouter()
#router.register(r'actors', ActorViewSet, base_name='ActorViewSet')
router.register(r'actors', ActorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]