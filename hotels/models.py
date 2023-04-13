from django.db import models

from users.models import User


class Activity(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"


class Loss(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"


class HotelType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    number_of_stars = models.IntegerField()
    single_rooms_count = models.IntegerField()
    double_rooms_count = models.IntegerField()
    president_rooms_count = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Hotel(models.Model):
    name = models.CharField(max_length=55)
    type = models.ForeignKey(to=HotelType, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    activities = models.ManyToManyField(to=Activity, through='HotelActivity')
    loss = models.ManyToManyField(to=Loss, through='HotelLoss')
    price_single_type_room = models.DecimalField(max_digits=10, decimal_places=2)
    price_double_type_room = models.DecimalField(max_digits=10, decimal_places=2)
    price_president_type_room = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.owner.first_name} {self.owner.last_name}"


class HotelActivity(models.Model):
    hotel = models.ForeignKey(to=Hotel, on_delete=models.CASCADE)
    activity = models.ForeignKey(to=Activity, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.hotel.name} - {self.activity.name}"


class HotelLoss(models.Model):
    hotel = models.ForeignKey(to=Hotel, on_delete=models.CASCADE)
    loss = models.ForeignKey(to=Loss, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.hotel.name} - {self.loss.name}"


class RoomType(models.Model):
    name = models.CharField(max_length=50)
    max_occupancy = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Room(models.Model):
    number = models.IntegerField()
    hotel = models.ForeignKey(to=Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(to=RoomType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.hotel.name} - {self.room_type}"
