from django.urls import path

from . import views

app_name = 'customers'

urlpatterns = [
    path('create/', views.create_customer_view, name='create'),
    path('display/', views.display_customers_view, name='display'),
    path('update/<int:customer_id>/', views.update_customer_view, name='update'),
    path('remove/<int:customer_id>/', views.remove_customer_view, name='remove'),
]
