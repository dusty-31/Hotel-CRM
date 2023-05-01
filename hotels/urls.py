from django.urls import path

from . import views

app_name = 'hotels'

urlpatterns = [
    path('create/', views.create_hotel_view, name='create_hotel'),
    path('display/', views.display_hotels_view, name='all_hotels_display'),
    path('display/<int:hotel_id>', views.display_one_hotel_view, name='display_hotel'),
    path('remove/<int:hotel_id>', views.remove_hotel_view, name='remove_hotel'),
    path('update/<int:hotel_id>', views.update_hotel_view, name='update_hotel'),
]
