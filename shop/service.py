from datetime import datetime

from shop.models import Shop
from shop.serializers import ShopSerializer


def get_city_from_db(request):
    shop = Shop.objects.all()

    street = request.query_params.get('street')
    city = request.query_params.get('city')
    is_open = request.query_params.get('open')

    if city is not None:
        shop = shop.filter(city__name=city)
    if street is not None:
        shop = shop.filter(street__name=street)
    if is_open is not None:
        if is_open == '1':
            shop = shop.filter(open_at__lte=datetime.now(), close_at__gte=datetime.now())
        elif is_open == '0':
            shop = shop.filter(open_at__gte=datetime.now())

    serializer = ShopSerializer(shop, many=True)
    return serializer.data
