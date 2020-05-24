from django.contrib import admin
from .models import Challenge, ChallengeOwner, TestCase

admin.site.register(Challenge)
admin.site.register(ChallengeOwner)
admin.site.register(TestCase)
