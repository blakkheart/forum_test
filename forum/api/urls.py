from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.views import AAA

router_v1 = DefaultRouter()

router_v1.register('', AAA, basename='aa')

urlpatterns = [
    path('', include(router_v1.urls))
]
