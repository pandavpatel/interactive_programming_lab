from django.db import models
from lab_app.models import Lab
from challenge_app.models import Challenge
from auth_app.models import User

class Submission(models.Model):
    submission_id = models.AutoField(auto_created=True, primary_key=True)
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    lab_id = models.ForeignKey(Lab, on_delete = models.CASCADE)
    challenge_id = models.ForeignKey(Challenge, on_delete = models.CASCADE)
    submission_datetime = models.DateTimeField(auto_now_add=True)
    solution_file = models.FileField(blank=False, null=False)
    testcase_results = models.CharField(max_length=1000, null=False)
    marks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return F"{self.username} {self.challenge_id}"