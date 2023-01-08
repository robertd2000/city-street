from rest_framework.serializers import ModelSerializer
from .models import City, Street, Country
from shop.serializers import ShopSerializer


class StreetSerializer(ModelSerializer):
    shop_set = ShopSerializer(many=True)

    class Meta:
        model = Street
        fields = ['name', 'city', 'shop_set']


class CitySerializer(ModelSerializer):
    street_set = StreetSerializer(many=True)

    class Meta:
        model = City
        fields = ['name', 'country', 'street_set']


class CityStreetsSerializer(ModelSerializer):
    street_set = StreetSerializer(many=True)

    class Meta:
        model = City
        fields = ['street_set']


class CountrySerializer(ModelSerializer):
    city_set = CitySerializer(many=True)

    class Meta:
        model = Country
        fields = ['name', 'country', 'city_set']
