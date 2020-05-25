from django.db import models
from auth_app.models import User

class Challenge(models.Model):
    challenge_id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=100, null=False)
    # Type of the description would later need to change as we would want to have rich text support
    description = models.CharField(max_length=10000, null=False)

    def __str__(self):
        return F"{self.title}"


class ChallengeOwner(models.Model):
    class Meta:
        unique_together = (('challenge_id', 'owner'),)

    challenge_owner_id = models.AutoField(auto_created=True, primary_key=True)
    challenge_id = models.ForeignKey(Challenge, on_delete = models.CASCADE)
    owner = models.ForeignKey(User, on_delete =  models.CASCADE)

    def __str__(self):
        return F"{self.owner} {self.challenge_id}"


class TestCase(models.Model):
    class Meta:
        unique_together = (('challenge_id', 'title'),)

    testcase_id = models.AutoField(auto_created=True, primary_key=True)
    challenge_id = models.ForeignKey(Challenge, on_delete = models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    input = models.FileField(blank=False, null=False)
    output = models.FileField(blank=False, null=False)
    marks = models.PositiveIntegerField(default=0)
    is_hidden = models.BooleanField(default=False)
    execution_time_limit = models.PositiveIntegerField(default=2000)

    def __str__(self):
        return F"{self.title}"