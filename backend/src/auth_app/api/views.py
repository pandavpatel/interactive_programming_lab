from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password

from ..models import User
from .serializers import UserSerializer


# Work in progress.....
# Added api directory to just show what folder structure we would be using for APIs


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@login_required
def users_v1(request):
    pass
