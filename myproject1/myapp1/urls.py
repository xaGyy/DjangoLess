from django.urls import path
from .views.views import sayHello, sayH1, car_list, get_brands, get_brands_by_country, get_vehicle_by_brand, get_vehicle_by_brands, addVehicle, deleteVehicle, getVehicleById, updateVehicle



from .views.cbv import Vehicle


urlpatterns = [
    path('hello', sayHello),
    path('h1', sayH1),
    path('cars/', car_list),
    path('cars/brand', get_vehicle_by_brand),
    path('cars/brands', get_vehicle_by_brands),
    path('brands', get_brands),
    path('brands/country', get_brands_by_country),

    path('cbv/vehicle', Vehicle.as_view(), name='add_page'),
    path('create/vehicle', addVehicle, name='add_page'),
    path('get/vehicle/<int:pk>', getVehicleById, name='get_page'),
    path('update/vehicle/<int:pk>', updateVehicle, name='update_page'),

]