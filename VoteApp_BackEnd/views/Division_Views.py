from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..serializers import DivisionSerializer
from ..models import Division
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
def get_divisions(request):
    user = request.user.id
    divisions = Division.objects.all()
    serializer = DivisionSerializer(divisions, many=True)
    return JsonResponse({'divisions': serializer.data}, safe=False, status=status.HTTP_200_OK)



@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_division(request, division_id):
    user = request.user.id
    division = Division.objects.get(id=division_id)
    serializer = DivisionSerializer(division, many=True)
    return JsonResponse({'division': serializer.data}, safe=False, status=status.HTTP_200_OK)




@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_division(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        division = Division.objects.create(
            code=payload["code"],
            caption=payload["caption"],
            is_Active=payload["is_Active"],
            added_by=user
        )
        serializer = DivisionSerializer(division)
        return JsonResponse({'division': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_division(request, division_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        # division_item = Division.objects.filter(id=division_id)
        # # returns 1 or 0
        # division_item.update(**payload)
        division = Division.objects.get(id=division_id)
        serializer = DivisionSerializer(division)
        return JsonResponse({'division': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_division(request, division_id):
    user = request.user.id
    try:
        division = Division.objects.get(id=division_id)
        division.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)