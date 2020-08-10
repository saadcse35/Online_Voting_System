from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(VoteInfo)
admin.site.register(Division)
admin.site.register(District)
admin.site.register(Upazila)
admin.site.register(UnionCouncil)
admin.site.register(Candidate)
admin.site.register(Voter)
admin.site.register(VoteCalculation)
admin.site.register(VoteWiseVoterList)
admin.site.register(Party)