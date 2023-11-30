from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app.models import Item
from app.serializers import ItemModelSerializer


class CreateItemAPIView(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemModelSerializer
    permission_classes = [IsAuthenticated]


