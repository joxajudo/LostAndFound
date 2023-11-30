from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import CreateItemAPIView

router = DefaultRouter()
router.register('', CreateItemAPIView)
# router.register('update/', ItemUpdateView)

urlpatterns = [
    # path('', CreateItemAPIView.as_view(), name='create-item'),
    path('', include(router.urls)),
]
