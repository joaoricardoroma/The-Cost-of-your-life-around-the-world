from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from ..documents import RestaurantDocument, RentMonthDocument, TransportationDocument, MarketDocument, SalariesDocument
from ..models import Restaurant, RentMonth, Market, Transportation, Salaries


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class Rent_monthSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentMonth
        fields = '__all__'


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'


class TransportationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportation
        fields = '__all__'


class SalariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salaries
        fields = '__all__'


# ElasticSearch


class RestaurantDocumentSerializer(DocumentSerializer):
    class Meta:
        document = RestaurantDocument
        fields = ['Meal', 'McDonalds', 'CokePepsi', 'Water']


class RentMonthDocumentSerializer(DocumentSerializer):
    class Meta:
        document = RentMonthDocument
        fields = ['in_City_Centre', 'Outside_of_Centre']


class MarketDocumentSerializer(DocumentSerializer):
    class Meta:
        document = MarketDocument
        fields = ['Milk', 'Rice', 'Eggs', 'Beef_Round']


class TransportationDocumentSerializer(DocumentSerializer):
    class Meta:
        document = TransportationDocument
        fields = ['One_way_Ticket', 'Taxi_1km', 'Gasoline']


class SalariesDocumentSerializer(DocumentSerializer):
    class Meta:
        document = SalariesDocument
        fields = ['Average_Monthly_Net_Salary']
