from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..serializers import VoteInfoSerializer
from ..models import VoteInfo
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
def get_vote_infos(request):
    user = request.user.id
    vote_infos = VoteInfo.objects.all()
    serializer = VoteInfoSerializer(vote_infos, many=True)
    return JsonResponse({'vote_infos': serializer.data}, safe=False, status=status.HTTP_200_OK)



@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_vote_info(request, vote_info_id):
    user = request.user.id
    vote_info = VoteInfo.objects.get(id=vote_info_id)
    serializer = VoteInfoSerializer(vote_info, many=True)
    return JsonResponse({'vote_info': serializer.data}, safe=False, status=status.HTTP_200_OK)




@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_vote_info(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        vote_info = VoteInfo.objects.create(
            code=payload["code"],
            caption=payload["caption"],
            is_Active=payload["is_Active"],
            added_by=user
        )
        serializer = VoteInfoSerializer(vote_info)
        return JsonResponse({'vote_info': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_vote_info(request, vote_info_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        # vote_info_item = VoteInfo.objects.filter(id=vote_info_id)
        # # returns 1 or 0
        # vote_info_item.update(**payload)
        vote_info = VoteInfo.objects.get(id=vote_info_id)
        serializer = VoteInfoSerializer(vote_info)
        return JsonResponse({'vote_info': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_vote_info(request, vote_info_id):
    user = request.user.id
    try:
        vote_info = VoteInfo.objects.get(id=vote_info_id)
        vote_info.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)