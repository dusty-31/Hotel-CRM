from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .services import (
    get_hotels_for_users,
    get_create_hotel_form,
    get_update_form_for_hotel,
    create_hotel,
    remove_hotel,
    update_hotel,
    get_hotel,
)


def index_view(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Hotels CRM - Admin Panel'
    }
    return render(request=request, template_name='hotels/index.html', context=context)


@login_required
def display_hotels_view(request: HttpRequest) -> HttpResponse:
    hotels = get_hotels_for_users(user_id=request.user.id)

    context = {
        'title': "Hotels CRM - My hotels",
        'hotels': hotels,
    }
    return render(request=request, template_name='hotels/list_hotels.html', context=context)


@login_required
def display_one_hotel_view(request: HttpRequest, hotel_id: int) -> HttpResponse:
    hotel = get_hotel(hotel_id=hotel_id)

    context = {
        'title': f"Hotel CRM - {hotel.name}",
        'hotel': hotel,
    }
    return render(request=request, template_name='hotels/hotel.html', context=context)


@login_required
def create_hotel_view(request: HttpRequest) -> HttpResponse:
    form = get_create_hotel_form(request=request)
    if request.method == "POST":
        create_hotel(user=request.user, form=form)
        return HttpResponseRedirect(reverse('hotels:all_hotels_display'))

    context = {
        'title': 'Hotels CRM - Create Hotel',
        'form': form,
    }
    return render(request=request, template_name='hotels/create_hotel.html', context=context)


@login_required
def remove_hotel_view(request: HttpRequest, hotel_id: int) -> HttpResponse:
    remove_hotel(hotel_id=hotel_id)
    return HttpResponseRedirect(reverse('hotels:all_hotels_display'))


@login_required
def update_hotel_view(request: HttpRequest, hotel_id: int):
    hotel = get_hotel(hotel_id=hotel_id)
    form = get_update_form_for_hotel(request=request, hotel_id=hotel_id)
    if request.method == "POST":
        update_hotel(form=form)
        return HttpResponseRedirect(reverse('hotels:all_hotels_display'))

    context = {
        'title': 'Hotel CRM - Update hotel',
        'hotel': hotel,
        'form': form,
    }
    return render(request=request, template_name='hotels/update_hotel.html', context=context)
