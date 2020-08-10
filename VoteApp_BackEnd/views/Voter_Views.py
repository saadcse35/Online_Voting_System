from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..serializers import VoterSerializer
from ..models import Voter
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
def get_voters(request):
    user = request.user.id
    voters = Voter.objects.all()
    serializer = VoterSerializer(voters, many=True)
    return JsonResponse({'voters': serializer.data}, safe=False, status=status.HTTP_200_OK)



@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_voter(request, voter_id):
    user = request.user.id
    voter = Voter.objects.get(id=voter_id)
    serializer = VoterSerializer(voter, many=True)
    return JsonResponse({'voter': serializer.data}, safe=False, status=status.HTTP_200_OK)




@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_voter(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        voter = Voter.objects.create(
            first_Name=payload["first_Name"],
            last_Name=payload["last_Name"],
            nid=payload["nid"],
            password=payload["password"],
            contact_No=payload["contact_No"],
            email=payload["email"],
            marital_Status=payload["marital_Status"],
            sex=payload["sex"],
            Division=payload["Division"],
            District=payload["District"],
            Upazila=payload["Upazila"],
            UnionCouncil=payload["UnionCouncil"],
            voter_area=payload["voter_area"],
            remk=payload["remk"],
            is_Active=payload["is_Active"],
            added_by=user
        )
        serializer = VoterSerializer(voter)
        return JsonResponse({'voter': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_voter(request, voter_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        # voter_item = Voter.objects.filter(id=voter_id)
        # # returns 1 or 0
        # voter_item.update(**payload)
        voter = Voter.objects.get(id=voter_id)
        serializer = VoterSerializer(voter)
        return JsonResponse({'voter': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_voter(request, voter_id):
    user = request.user.id
    try:
        voter = Voter.objects.get(id=voter_id)
        voter.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)