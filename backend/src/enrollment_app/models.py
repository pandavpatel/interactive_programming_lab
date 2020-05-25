from django.db import models
from auth_app.models import User

class Subject(models.Model):
    subject_id = models.AutoField(auto_created=True, primary_key=True)
    subject_name = models.CharField(max_length=50, null=False)
    year_offered = models.PositiveIntegerField(default=0, null=False)

    def __str__(self):
        return F"{self.year_offered} {self.subject_name}"


class Enrollment(models.Model):
    class Meta:
        unique_together = (('subject_id', 'username'),)

    enrollment_id = models.AutoField(auto_created=True, primary_key=True)
    subject_id = models.ForeignKey(Subject, on_delete = models.CASCADE)
    username = models.ForeignKey(User, on_delete =  models.CASCADE)
    batch = models.CharField(max_length=10, null=True)

    def __str__(self):
        return F"{self.batch} {self.username} {self.subject_id}"