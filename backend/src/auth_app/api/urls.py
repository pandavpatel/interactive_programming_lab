from django.urls import path
from .views import users_v1

urlpatterns = [
    path('api/v1/users/', users_v1, name='users_v1'),
]
