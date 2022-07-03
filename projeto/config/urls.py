"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from app.api import viewsets as restaurant_viewsets
from app.api import viewsets as rentmonth_viewsets
from app.api import viewsets as market_viewsets
from app.api import viewsets as transportation_viewsets
from app.api import viewsets as salaries_viewsets

from app.api.viewsets import RestaurantDocumentWithESViewSet, RentMonthWithESViewSet, MarketDocumentWithESViewSet, \
    TransportationDocumentWithESViewSet

route = routers.DefaultRouter()

route.register(r'restaurant', restaurant_viewsets.RestaurantViewSet, basename="Restaurant")
route.register(r'rentmonth', rentmonth_viewsets.RentmonthViewSet, basename="Rent_month")
route.register(r'market', market_viewsets.MarketViewSet, basename="Market")
route.register(r'transportation', transportation_viewsets.TransportationViewSet, basename="Transportation")
route.register(r'salaries', salaries_viewsets.SalariesViewSet, basename="Salaries")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('restaurant/search/', RestaurantDocumentWithESViewSet.as_view({'get': 'list'}), name='restaurant'),
    path('rent_month/search/', RentMonthWithESViewSet.as_view({'get': 'list'}), name='rent_month'),
    path('market/search/', MarketDocumentWithESViewSet.as_view({'get': 'list'}), name='market'),
    path('transportation/search/', TransportationDocumentWithESViewSet.as_view({'get': 'list'}), name='transportation'),
]
