from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import CustomerCreateForm


@login_required
def customer_create_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomerCreateForm(data=request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.created_by = request.user
            customer.save()

            return HttpResponseRedirect(reverse('index'))
    else:
        form = CustomerCreateForm()
    context = {
        'form': form,
    }

    return render(request=request, template_name='customers/create_form.html', context=context)
