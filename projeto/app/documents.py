from django_elasticsearch_dsl import Document, fields, Index
from django_elasticsearch_dsl.registries import registry
from .models import Restaurant, RentMonth, Market, Transportation, Salaries


@registry.register_document
class RestaurantDocument(Document):

    class Index:
        name = 'restaurant'
        setting = {
            'number_of_shards': 1,
            'number_of_replicas': 1
        }

    class Django:
        model = Restaurant

        fields = ['Meal', 'McDonalds', 'CokePepsi', 'Water']


@registry.register_document
class RentMonthDocument(Document):

    class Index:
        name = 'rentmonth'
        setting = {
            'number_of_shards': 1,
            'number_of_replicas': 1
        }

    class Django:
        model = RentMonth

        fields = ['in_City_Centre', 'Outside_of_Centre']


@registry.register_document
class MarketDocument(Document):

    class Index:
        name = 'market'
        setting = {
            'number_of_shards': 1,
            'number_of_replicas': 1
        }

    class Django:
        model = Market

        fields = ['Milk', 'Rice', 'Eggs', 'Beef_Round']


@registry.register_document
class TransportationDocument(Document):

    class Index:
        name = 'transportation'
        setting = {
            'number_of_shards': 1,
            'number_of_replicas': 1
        }

    class Django:
        model = Transportation

        fields = ['One_way_Ticket', 'Taxi_1km', 'Gasoline']


class SalariesDocument(Document):

    class Index:
        name = 'salaries'
        setting = {
            'number_of_shards': 1,
            'number_of_replicas': 1
        }

    class Django:
        model = Salaries

        fields = ['Average_Monthly_Net_Salary']