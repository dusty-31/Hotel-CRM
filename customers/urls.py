from django.urls import path

from . import views

app_name = 'customers'

urlpatterns = [
    path('create/', views.create_customer_view, name='create_customer'),
    path('display/', views.display_customers_view, name='all_customers_display'),
    path('display/<int:customer_id>', views.display_one_customer_view, name='display_customer'),
    path('update/<int:customer_id>/', views.update_customer_view, name='update_customer'),
    path('remove/<int:customer_id>/', views.remove_customer_view, name='remove_customer'),
]
