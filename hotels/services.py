from typing import Any

from django.shortcuts import get_object_or_404
from django.db.models import QuerySet
from django.http import HttpRequest

from users.models import User

from .forms import CreateHotelForm, UpdateHotelForm
from .models import Hotel, RoomType, Room


def get_hotels_for_users(user_id: int) -> QuerySet:
    hotels = Hotel.objects.filter(owner_id=user_id)
    return hotels


def get_create_hotel_form(request: HttpRequest) -> CreateHotelForm:
    if request.method == "POST":
        form = CreateHotelForm(data=request.POST)
    else:
        form = CreateHotelForm()

    return form


def create_hotel(user: User, form: CreateHotelForm) -> None:
    if form.is_valid():
        hotel = form.save(commit=False)
        hotel.owner_id = user.id
        hotel.save()
        _create_rooms_for_hotel(hotel=hotel)


def remove_hotel(hotel_id: int) -> None:
    hotel = get_hotel(hotel_id=hotel_id)
    hotel.delete()


def update_hotel(form: UpdateHotelForm) -> None:
    if form.is_valid():
        form.save()


def get_update_form_for_hotel(request: HttpRequest, hotel_id: int) -> UpdateHotelForm:
    current_hotel = get_hotel(hotel_id=hotel_id)
    if request.method == "POST":
        form = UpdateHotelForm(data=request.POST, instance=current_hotel)
    else:
        form = UpdateHotelForm(instance=current_hotel)
    return form


def get_hotel(hotel_id: int) -> Any:
    return get_object_or_404(klass=Hotel, pk=hotel_id)


def _create_rooms_for_hotel(hotel: Hotel) -> None:
    counter = 1
    room_types = RoomType.objects.all()
    for room_type in room_types:
        count_field = f"{room_type.name.split()[0].lower()}_rooms_count"
        count = getattr(hotel.type, count_field)
        price_field = f"price_{room_type.name.split()[0].lower()}_type_room"
        price = getattr(hotel, price_field)
        _create_rooms_by_type(room_type=room_type,
                              hotel=hotel,
                              counter=counter,
                              count_rooms=count,
                              price=price
                              )


def _create_rooms_by_type(room_type: RoomType, hotel: Hotel, counter: int, count_rooms: int, price: float) -> None:
    for _ in range(count_rooms):
        Room.objects.create(number=counter,
                            hotel=hotel,
                            room_type=room_type,
                            price=price)
