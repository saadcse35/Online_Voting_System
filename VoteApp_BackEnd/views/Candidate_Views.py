from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..serializers import CandidateSerializer
from ..models import Candidate
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
def get_candidates(request):
    user = request.user.id
    candidates = Candidate.objects.all()
    serializer = CandidateSerializer(candidates, many=True)
    return JsonResponse({'candidates': serializer.data}, safe=False, status=status.HTTP_200_OK)



@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_candidate(request, candidate_id):
    user = request.user.id
    candidate = Candidate.objects.get(id=candidate_id)
    serializer = CandidateSerializer(candidate, many=True)
    return JsonResponse({'candidate': serializer.data}, safe=False, status=status.HTTP_200_OK)




@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_candidate(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        candidate = Candidate.objects.create(
            caption=payload["caption"],
            Party=payload["Party"],
            VoteInfo=payload["VoteInfo"],
            User=payload["User"],
            Voter=payload["Voter"],
            remk=payload["remk"],
            is_Active=payload["is_Active"],
            added_by=user
        )
        serializer = CandidateSerializer(candidate)
        return JsonResponse({'candidate': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_candidate(request, candidate_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        # candidate_item = Candidate.objects.filter(id=candidate_id)
        # # returns 1 or 0
        # candidate_item.update(**payload)
        candidate = Candidate.objects.get(id=candidate_id)
        serializer = CandidateSerializer(candidate)
        return JsonResponse({'candidate': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_candidate(request, candidate_id):
    user = request.user.id
    try:
        candidate = Candidate.objects.get(id=candidate_id)
        candidate.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)