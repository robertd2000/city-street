from rest_framework.serializers import ModelSerializer
from .models import Shop
from city.models import City, Street


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'country']


class StreetSerializer(ModelSerializer):
    class Meta:
        model = Street
        fields = ['name', 'city']


class ShopSerializer(ModelSerializer):
    city = CitySerializer()
    street = StreetSerializer()

    class Meta:
        model = Shop
        fields = ['id', 'name', 'city', 'street', 'house', 'open_at', 'close_at']


class ShopCreateSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'city', 'street', 'house', 'open_at', 'close_at']
