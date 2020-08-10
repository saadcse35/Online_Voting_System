from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..serializers import UnionCouncilSerializer
from ..models import UnionCouncil
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
def get_union_councils(request):
    user = request.user.id
    union_councils = UnionCouncil.objects.all()
    serializer = UnionCouncilSerializer(union_councils, many=True)
    return JsonResponse({'union_councils': serializer.data}, safe=False, status=status.HTTP_200_OK)



@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_union_council(request, union_council_id):
    user = request.user.id
    union_council = UnionCouncil.objects.get(id=union_council_id)
    serializer = UnionCouncilSerializer(union_council, many=True)
    return JsonResponse({'union_council': serializer.data}, safe=False, status=status.HTTP_200_OK)




@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_union_council(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        union_council = UnionCouncil.objects.create(
            code=payload["code"],
            caption=payload["caption"],
            Upazila=payload["Upazila"],
            District=payload["District"],
            Division=payload["Division"],
            is_Active=payload["is_Active"],
            added_by=user
        )
        serializer = UnionCouncilSerializer(union_council)
        return JsonResponse({'union_council': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_union_council(request, union_council_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        # union_council_item = UnionCouncil.objects.filter(id=union_council_id)
        # # returns 1 or 0
        # union_council_item.update(**payload)
        union_council = UnionCouncil.objects.get(id=union_council_id)
        serializer = UnionCouncilSerializer(union_council)
        return JsonResponse({'union_council': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_union_council(request, union_council_id):
    user = request.user.id
    try:
        union_council = UnionCouncil.objects.get(id=union_council_id)
        union_council.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)