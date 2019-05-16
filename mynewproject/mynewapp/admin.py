from django.contrib import admin
from mynewapp.models import Candidate, CandidateInfo, CandidateAddress

# Register your models here.

admin.site.register(Candidate)
admin.site.register(CandidateInfo)
admin.site.register(CandidateAddress)