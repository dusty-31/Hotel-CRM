from typing import Any

from django.shortcuts import get_object_or_404
from django.db.models import QuerySet
from django.http import HttpRequest
from django.contrib import messages

from .forms import CustomerCreateForm, CustomerUpdateForm
from .models import Customer
from users.models import User


def get_customers_for_user(user_id: int) -> QuerySet:
    customers = Customer.objects.filter(created_by=user_id)
    return customers


def create_customer(request: HttpRequest, user: User, form: CustomerCreateForm) -> None:
    if form.is_valid():
        _save_customer(user=user, form=form)
        messages.success(request=request, message="Created successfully")


def remove_customer(request: HttpRequest, customer_id: int) -> None:
    customer = get_customer(customer_id)
    customer.delete()
    messages.success(request=request, message=f"Removed {customer.first_name} {customer.last_name} successfully")


def update_customer(request: HttpRequest, form: CustomerUpdateForm) -> None:
    if form.is_valid():
        form.save()
        messages.success(request=request, message="Saved successfully!")


def get_customer_create_form(request: HttpRequest) -> CustomerCreateForm:
    if request.method == "POST":
        form = CustomerCreateForm(data=request.POST)
    else:
        form = CustomerCreateForm()

    return form


def get_customer_update_form(request: HttpRequest, customer_id: int) -> CustomerUpdateForm:
    customer = get_customer(customer_id=customer_id)
    if request.method == "POST":
        form = CustomerUpdateForm(data=request.POST, instance=customer)
    else:
        form = CustomerUpdateForm(instance=customer)

    return form


def get_customer(customer_id: int) -> Any:
    return get_object_or_404(klass=Customer, pk=customer_id)


def _save_customer(user: User, form: CustomerCreateForm) -> None:
    customer = form.save(commit=False)
    customer.created_by = user
    customer.save()
