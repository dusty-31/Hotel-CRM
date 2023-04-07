from typing import Union

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .services import (
    get_customers_for_user,
    get_customer_create_form,
    create_customer,
    remove_customer,
    update_customer,
    get_customer_update_form,
    get_customer
)


@login_required
def display_customers_view(request: HttpRequest) -> HttpResponse:
    customers = get_customers_for_user(request.user.id)

    context = {
        'title': "CRM Hotels - Customers",
        'customers': customers,
    }
    return render(request=request, template_name='customers/display_customers.html', context=context)


@login_required
def create_customer_view(request: HttpRequest) -> Union[HttpResponse, HttpResponseRedirect]:
    form = get_customer_create_form(request=request)
    if request.method == "POST":
        create_customer(request=request, user=request.user, form=form)

        return HttpResponseRedirect(reverse('customers:display'))

    context = {
        'form': form,
    }
    return render(request=request, template_name='customers/create_form.html', context=context)


@login_required
def remove_customer_view(request: HttpRequest, customer_id: int) -> HttpResponseRedirect:
    remove_customer(request=request, customer_id=customer_id)

    return HttpResponseRedirect(reverse('customers:display'))


@login_required
def update_customer_view(request: HttpRequest, customer_id: int) -> Union[HttpResponse, HttpResponseRedirect]:
    customer = get_customer(customer_id=customer_id)
    form = get_customer_update_form(request=request, customer_id=customer_id)
    if request.method == "POST":
        update_customer(request=request, form=form)
        return HttpResponseRedirect(request.META["HTTP_REFERER"])

    context = {
        "form": form,
        "customer": customer,
    }
    return render(request=request, template_name='customers/update_form.html', context=context)
