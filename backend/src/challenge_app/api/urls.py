from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('challenge/', login_required(views.ChallengeDetails.as_view()), name='challenge'),
    path('challenge-list/', login_required(views.ChallengeList.as_view()), name='challenge-list'),
    path('challenge-edit/<int:challenge_id>)/', login_required(views.ChallengeEdit.as_view()), name='challenge-edit'),
]
