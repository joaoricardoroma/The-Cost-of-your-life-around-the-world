from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework import viewsets

from .serializers import RestaurantDocumentSerializer, RentMonthDocumentSerializer, MarketDocumentSerializer, \
    TransportationDocumentSerializer, SalariesDocumentSerializer
from ..api import serializers
from ..documents import RestaurantDocument, RentMonthDocument, MarketDocument, TransportationDocument, SalariesDocument
from ..models import Restaurant, RentMonth, Market, Transportation, Salaries


class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RestaurantSerializer
    queryset = Restaurant.objects.all()


class RentmonthViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Rent_monthSerializer
    queryset = RentMonth.objects.all()


class MarketViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MarketSerializer
    queryset = Market.objects.all()


class TransportationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TransportationSerializer
    queryset = Transportation.objects.all()


class SalariesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SalariesSerializer
    queryset = Salaries.objects.all()


# ElasticSearch

class RestaurantDocumentWithESViewSet(DocumentViewSet):
    document = RestaurantDocument
    serializer_class = RestaurantDocumentSerializer

    filter_backends = [SearchFilterBackend]

    search_fields = ['Meal', 'McDonalds', 'CokePepsi', 'Water']

    filter_fields = ['Meal', 'McDonalds', 'CokePepsi', 'Water']


class RentMonthWithESViewSet(DocumentViewSet):
    document = RentMonthDocument
    serializer_class = RentMonthDocumentSerializer

    filter_backends = [SearchFilterBackend]

    search_fields = ['in_City_Centre', 'Outside_of_Centre']

    filter_fields = ['in_City_Centre', 'Outside_of_Centre']


class MarketDocumentWithESViewSet(DocumentViewSet):
    document = MarketDocument
    serializer_class = MarketDocumentSerializer

    filter_backends = [SearchFilterBackend]

    search_fields = ['Milk', 'Rice', 'Eggs', 'Beef_Round']

    filter_fields = ['Milk', 'Rice', 'Eggs', 'Beef_Round']


class TransportationDocumentWithESViewSet(DocumentViewSet):
    document = TransportationDocument
    serializer_class = TransportationDocumentSerializer

    filter_backends = [SearchFilterBackend]

    search_fields = ['One_way_Ticket', 'Taxi_1km', 'Gasoline']

    filter_fields = ['One_way_Ticket', 'Taxi_1km', 'Gasoline']


class SalariesDocumentWithESViewSet(DocumentViewSet):
    document = SalariesDocument
    serializer_class = SalariesDocumentSerializer

    filter_backends = [SearchFilterBackend]

    search_fields = ['Average_Monthly_Net_Salary']

    filter_fields = ['Average_Monthly_Net_Salary']