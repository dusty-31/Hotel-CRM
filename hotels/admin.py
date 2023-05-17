from django.contrib import admin

from .models import (
    Hotel,
    HotelType,
    RoomType,
    Room,
    Activity,
    HotelActivity,
)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass


@admin.register(HotelType)
class HotelTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass


@admin.register(HotelActivity)
class HotelActivityAdmin(admin.ModelAdmin):
    pass
