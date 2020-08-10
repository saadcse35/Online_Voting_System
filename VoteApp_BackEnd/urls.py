from django.urls import path
from . import views

# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('getalldivisions', views.get_divisions),
    path('getdivision', views.get_division),
    path('adddivision', views.add_division),
    path('updatedivision/<int:division_id>', views.update_division),
    path('deletedivision/<int:division_id>', views.delete_division),

    path('getalldistricts', views.get_districts),
    path('getdistrict', views.get_district),
    path('adddistrict', views.add_district),
    path('updatedistrict/<int:district_id>', views.update_district),
    path('deletedistrict/<int:district_id>', views.delete_district),

    path('getallupazilas', views.get_upazilas),
    path('getupazila', views.get_upazila),
    path('addupazila', views.add_upazila),
    path('updateupazila/<int:upazila_id>', views.update_upazila),
    path('deleteupazila/<int:upazila_id>', views.delete_upazila),

    path('getallunion_councils', views.get_union_councils),
    path('getunion_council', views.get_union_council),
    path('addunion_council', views.add_union_council),
    path('updateunion_council/<int:union_council_id>', views.update_union_council),
    path('deleteunion_council/<int:union_council_id>', views.delete_union_council),

    path('getallcandidates', views.get_candidates),
    path('getcandidate', views.get_candidate),
    path('addcandidate', views.add_candidate),
    path('updatecandidate/<int:candidate_id>', views.update_candidate),
    path('deletecandidate/<int:candidate_id>', views.delete_candidate),

    path('getallpartys', views.get_partys),
    path('getparty', views.get_party),
    path('addparty', views.add_party),
    path('updateparty/<int:party_id>', views.update_party),
    path('deleteparty/<int:party_id>', views.delete_party),

    path('getallvote_infos', views.get_vote_infos),
    path('getvote_info', views.get_vote_info),
    path('addvote_info', views.add_vote_info),
    path('updatevote_info/<int:vote_info_id>', views.update_vote_info),
    path('deletevote_info/<int:vote_info_id>', views.delete_vote_info),

    path('getallvoters', views.get_voters),
    path('getvoter', views.get_voter),
    path('addvoter', views.add_voter),
    path('updatevoter/<int:voter_id>', views.update_voter),
    path('deletevoter/<int:voter_id>', views.delete_voter),

    path('getallvote_wise_voters', views.get_vote_wise_voters),
    path('getvote_wise_voter', views.get_vote_wise_voter),
    path('addvote_wise_voter', views.add_vote_wise_voter),
    path('updatevote_wise_voter/<int:vote_wise_voter_id>', views.update_vote_wise_voter),
    path('deletevote_wise_voter/<int:vote_wise_voter_id>', views.delete_vote_wise_voter),

]

# urlpatterns = format_suffix_patterns(urlpatterns)
