from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .viewsets import HorizonViewSet, UserViewSet, CityViewSet, TrajectoryViewSet
from django.urls import path
from .views import UserCreate

router = routers.SimpleRouter()
router.register('horizon', HorizonViewSet)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cities', CityViewSet)
router.register(r'trajectories', TrajectoryViewSet)

urlpatterns = router.urls 

urlpatterns = [
    path('api/form-submit/', UserCreate.as_view()),
]
