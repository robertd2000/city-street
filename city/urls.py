from django.urls import path
from .views import Cities, CityStreets


urlpatterns = [
    path('', Cities.as_view(), name='get_cities'),
    path('<int:pk>/streets/', CityStreets.as_view(), name='get_city_streets'),
]
