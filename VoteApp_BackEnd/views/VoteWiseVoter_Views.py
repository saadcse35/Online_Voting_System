from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..serializers import VoteWiseVoterListSerializer
from ..models import VoteWiseVoterList
from rest_framework import status

import json
from django.core.exceptions import ObjectDoesNotExist

# @api_view(["GET"])
# @csrf_exempt
# @permission_classes([IsAuthenticated])
# def welcome(request):
#     content = {"message": "Welcome to the BookStore!"}
#     return JsonResponse(content)



@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_vote_wise_voters(request):
    user = request.user.id
    vote_wise_voters = VoteWiseVoterList.objects.all()
    serializer = VoteWiseVoterListSerializer(vote_wise_voters, many=True)
    return JsonResponse({'vote_wise_voters': serializer.data}, safe=False, status=status.HTTP_200_OK)



@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_vote_wise_voter(request, vote_wise_voter_id):
    user = request.user.id
    vote_wise_voter = VoteWiseVoterList.objects.get(id=vote_wise_voter_id)
    serializer = VoteWiseVoterListSerializer(vote_wise_voter, many=True)
    return JsonResponse({'vote_wise_voter': serializer.data}, safe=False, status=status.HTTP_200_OK)




@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_vote_wise_voter(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        vote_wise_voter = VoteWiseVoterList.objects.create(
            VoteInfo=payload["VoteInfo"],
            Voter=payload["Voter"],
            nid=payload["nid"],
            tokenNumber=payload["tokenNumber"],
            added_by=user
        )
        serializer = VoteWiseVoterListSerializer(vote_wise_voter)
        return JsonResponse({'vote_wise_voter': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_vote_wise_voter(request, vote_wise_voter_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        # vote_wise_voter_item = VoteWiseVoterList.objects.filter(id=vote_wise_voter_id)
        # # returns 1 or 0
        # vote_wise_voter_item.update(**payload)
        vote_wise_voter = VoteWiseVoterList.objects.get(id=vote_wise_voter_id)
        serializer = VoteWiseVoterListSerializer(vote_wise_voter)
        return JsonResponse({'vote_wise_voter': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_vote_wise_voter(request, vote_wise_voter_id):
    user = request.user.id
    try:
        vote_wise_voter = VoteWiseVoterList.objects.get(id=vote_wise_voter_id)
        vote_wise_voter.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)