from rest_framework.serializers import ModelSerializer

from app.models import Item


class ItemModelSerializer(ModelSerializer):
    class Meta:
        model = Item
        exclude = ()

