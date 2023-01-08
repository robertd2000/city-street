from rest_framework import generics
from rest_framework.response import Response
from .serializers import ShopCreateSerializer
from .models import Shop
from .service import get_city_from_db


class ShopView(generics.GenericAPIView):
    serializer_class = ShopCreateSerializer
    queryset = Shop.objects.all()

    def post(self, request):
        serializer = ShopCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def get(self, request):
        shop = get_city_from_db(request)
        return Response(shop)
