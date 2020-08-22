from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import VoteInfo
from ..serializers import VoteInfoSerializer


@api_view(['GET', 'POST'])
def voteInfo_listCreate(request):
    """
    List all code voteInfos, or create a new voteInfo.
    """
    if request.method == 'GET':
        voteInfos = VoteInfo.objects.all()
        serializer = VoteInfoSerializer(voteInfos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VoteInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def voteInfo_detail(request, id):
    """
    Retrieve, update or delete a code voteInfo.
    """
    try:
        voteInfo = VoteInfo.objects.get(id=id)
    except VoteInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VoteInfoSerializer(voteInfo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VoteInfoSerializer(voteInfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        voteInfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)