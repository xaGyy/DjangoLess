from django.urls import path
from .views import registration

urlpatterns = [
    path("signup", registration, name="add_user")
]