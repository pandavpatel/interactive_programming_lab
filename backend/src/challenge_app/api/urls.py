from django.urls import path
from . import views

urlpatterns = [
    path('challenge/', views.ChallengeDetails.as_view(), name='challenge'),
    path('challenge-list/', views.ChallengeList.as_view(), name='challenge-list'),
    path('challenge-edit/<int:challenge_id>)/', views.ChallengeEdit.as_view(), name='challenge-edit'),
]
