from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..serializers import VoteCalculationSerializer
from ..models import VoteCalculation
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
def get_vote_calculations(request):
    user = request.user.id
    vote_calculations = VoteCalculation.objects.all()
    serializer = VoteCalculationSerializer(vote_calculations, many=True)
    return JsonResponse({'vote_calculations': serializer.data}, safe=False, status=status.HTTP_200_OK)



@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_vote_calculation(request, vote_calculation_id):
    user = request.user.id
    vote_calculation = VoteCalculation.objects.get(id=vote_calculation_id)
    serializer = VoteCalculationSerializer(vote_calculation, many=True)
    return JsonResponse({'vote_calculation': serializer.data}, safe=False, status=status.HTTP_200_OK)




@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_vote_calculation(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        vote_calculation = VoteCalculation.objects.create(
            code=payload["code"],
            VoteInfo=payload["VoteInfo"],
            Candidate=payload["Candidate"],
            User=payload["User"],
            is_Active=payload["is_Active"],
            added_by=user
        )
        serializer = VoteCalculationSerializer(vote_calculation)
        return JsonResponse({'vote_calculation': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_vote_calculation(request, vote_calculation_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        # vote_calculation_item = VoteCalculation.objects.filter(id=vote_calculation_id)
        # # returns 1 or 0
        # vote_calculation_item.update(**payload)
        vote_calculation = VoteCalculation.objects.get(id=vote_calculation_id)
        serializer = VoteCalculationSerializer(vote_calculation)
        return JsonResponse({'vote_calculation': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_vote_calculation(request, vote_calculation_id):
    user = request.user.id
    try:
        vote_calculation = VoteCalculation.objects.get(id=vote_calculation_id)
        vote_calculation.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)