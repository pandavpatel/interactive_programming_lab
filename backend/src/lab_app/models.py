from django.db import models
from enrollment_app.models import Subject
from challenge_app.models import Challenge

class Lab(models.Model):
    class Meta:
        unique_together = (('subject_id', 'lab_number'),)

    lab_id = models.AutoField(auto_created=True, primary_key=True)
    subject_id = models.ForeignKey(Subject, on_delete = models.CASCADE)
    lab_number = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=100, null=False)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return F"{self.lab_number} {self.title}"


class LabChallenge(models.Model):
    class Meta:
        unique_together = (('lab_id', 'challenge_id'),)

    lab_challenge_id = models.AutoField(auto_created=True, primary_key=True)
    lab_id = models.ForeignKey(Lab, on_delete =  models.CASCADE)
    challenge_id = models.ForeignKey(Challenge, on_delete = models.CASCADE)
    challenge_number = models.PositiveIntegerField(default=0)
    marks = models.PositiveIntegerField(default=10)

    def __str__(self):
        return F"{self.challenge_number}"


class ProgrammingLanguage(models.Model):
    programming_language_id = models.AutoField(auto_created=True, primary_key=True)
    programming_language_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return F"{self.programming_language_name}"

class LabChallengeProgrammingLanguage(models.Model):
    class Meta:
        unique_together = (('lab_challenge_id', 'programming_language_id'),)

    lab_challenge_programming_language_id = models.AutoField(auto_created=True, primary_key=True)
    lab_challenge_id = models.ForeignKey(LabChallenge, on_delete =  models.CASCADE)
    programming_language_id = models.ForeignKey(ProgrammingLanguage, on_delete =  models.CASCADE)
