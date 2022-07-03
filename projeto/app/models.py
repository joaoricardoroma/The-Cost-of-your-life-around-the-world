from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models


# class Profile(models.Model):
#     user = models.ForeignKey(User)


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4, unique=True)
    Meal = models.FloatField()
    McDonalds = models.FloatField()
    CokePepsi = models.FloatField()
    Water = models.FloatField()


class Market(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4, unique=True)
    Milk = models.FloatField()
    Rice = models.FloatField()
    Eggs = models.FloatField()
    Beef_Round = models.FloatField()


class Transportation(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4, unique=True)
    One_way_Ticket = models.FloatField()
    Taxi_1km = models.FloatField()
    Gasoline = models.FloatField()


class RentMonth(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4, unique=True)
    in_City_Centre = models.FloatField()
    Outside_of_Centre = models.FloatField()
    flag_country = models.FileField()


class Salaries(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4, unique=True)
    Average_Monthly_Net_Salary = models.FloatField()

