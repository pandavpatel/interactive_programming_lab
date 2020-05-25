from django.contrib import admin
from .models import Lab, LabChallenge, ProgrammingLanguage, LabChallengeProgrammingLanguage

admin.site.register(Lab)
admin.site.register(LabChallenge)
admin.site.register(ProgrammingLanguage)
admin.site.register(LabChallengeProgrammingLanguage)