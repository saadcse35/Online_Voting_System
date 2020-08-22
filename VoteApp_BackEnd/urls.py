from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('divisions/', views.division_listCreate),
    path('divisions/<int:id>', views.division_detail),

    path('districts/', views.district_listCreate),
    path('districts/<int:id>', views.district_detail),

    path('upazilas/', views.upazila_listCreate),
    path('upazilas/<int:id>', views.upazila_detail),

    path('unionCouncils/', views.unionCouncil_listCreate),
    path('unionCouncils/<int:id>', views.unionCouncil_detail),

    path('candidates/', views.candidate_listCreate),
    path('candidates/<int:id>', views.candidate_detail),

    path('parties/', views.party_listCreate),
    path('parties/<int:id>', views.party_detail),

    path('voteInfos/', views.voteInfo_listCreate),
    path('voteInfos/<int:id>', views.voteInfo_detail),

    path('voters/', views.voter_listCreate),
    path('voters/<int:id>', views.voter_detail),

    path('voteWiseVoters/', views.voteWiseVoter_listCreate),
    path('voteWiseVoters/<int:id>', views.voteWiseVoter_detail),

    path('voteCalculations/', views.voteCalculation_listCreate),
    path('voteCalculations/<int:id>', views.voteCalculation_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)
