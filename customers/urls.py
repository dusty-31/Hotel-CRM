from django.urls import path

from . import views

app_name = 'customers'

urlpatterns = [
    path('create/', views.customer_create_view, name='customer-create'),
]
