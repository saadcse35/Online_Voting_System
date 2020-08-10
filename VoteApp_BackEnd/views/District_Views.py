from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..serializers import DistrictSerializer
from ..models import District
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
def get_districts(request):
    user = request.user.id
    districts = District.objects.all()
    serializer = DistrictSerializer(districts, many=True)
    return JsonResponse({'districts': serializer.data}, safe=False, status=status.HTTP_200_OK)



@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_district(request, district_id):
    user = request.user.id
    district = District.objects.get(id=district_id)
    serializer = DistrictSerializer(district, many=True)
    return JsonResponse({'district': serializer.data}, safe=False, status=status.HTTP_200_OK)




@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_district(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        district = District.objects.create(
            code=payload["code"],
            caption=payload["caption"],
            Division=payload["Division"],
            is_Active=payload["is_Active"],
            added_by=user
        )
        serializer = DistrictSerializer(district)
        return JsonResponse({'district': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_district(request, district_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        # district_item = District.objects.filter(id=district_id)
        # # returns 1 or 0
        # district_item.update(**payload)
        district = District.objects.get(id=district_id)
        serializer = DistrictSerializer(district)
        return JsonResponse({'district': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_district(request, district_id):
    user = request.user.id
    try:
        district = District.objects.get(id=district_id)
        district.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)