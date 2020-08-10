from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..serializers import UpazilaSerializer
from ..models import Upazila
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
def get_upazilas(request):
    user = request.user.id
    upazilas = Upazila.objects.all()
    serializer = UpazilaSerializer(upazilas, many=True)
    return JsonResponse({'upazilas': serializer.data}, safe=False, status=status.HTTP_200_OK)



@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_upazila(request, upazila_id):
    user = request.user.id
    upazila = Upazila.objects.get(id=upazila_id)
    serializer = UpazilaSerializer(upazila, many=True)
    return JsonResponse({'upazila': serializer.data}, safe=False, status=status.HTTP_200_OK)




@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_upazila(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        upazila = Upazila.objects.create(
            code=payload["code"],
            caption=payload["caption"],
            District=payload["District"],
            Division=payload["Division"],
            is_Active=payload["is_Active"],
            added_by=user
        )
        serializer = UpazilaSerializer(upazila)
        return JsonResponse({'upazila': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_upazila(request, upazila_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        # upazila_item = Upazila.objects.filter(id=upazila_id)
        # # returns 1 or 0
        # upazila_item.update(**payload)
        upazila = Upazila.objects.get(id=upazila_id)
        serializer = UpazilaSerializer(upazila)
        return JsonResponse({'upazila': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_upazila(request, upazila_id):
    user = request.user.id
    try:
        upazila = Upazila.objects.get(id=upazila_id)
        upazila.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)