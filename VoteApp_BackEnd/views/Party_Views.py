from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..serializers import PartySerializer
from ..models import Party
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
def get_partys(request):
    user = request.user.id
    partys = Party.objects.all()
    serializer = PartySerializer(partys, many=True)
    return JsonResponse({'partys': serializer.data}, safe=False, status=status.HTTP_200_OK)



@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_party(request, party_id):
    user = request.user.id
    party = Party.objects.get(id=party_id)
    serializer = PartySerializer(party, many=True)
    return JsonResponse({'party': serializer.data}, safe=False, status=status.HTTP_200_OK)




@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_party(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        party = Party.objects.create(
            code=payload["code"],
            caption=payload["caption"],
            icon=payload["icon"],
            desc=payload["desc"],
            remk=payload["remk"],
            is_Active=payload["is_Active"],
            added_by=user
        )
        serializer = PartySerializer(party)
        return JsonResponse({'party': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_party(request, party_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        # party_item = Party.objects.filter(id=party_id)
        # # returns 1 or 0
        # party_item.update(**payload)
        party = Party.objects.get(id=party_id)
        serializer = PartySerializer(party)
        return JsonResponse({'party': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_party(request, party_id):
    user = request.user.id
    try:
        party = Party.objects.get(id=party_id)
        party.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)