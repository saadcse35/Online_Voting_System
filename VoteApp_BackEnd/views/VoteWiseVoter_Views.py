from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import VoteWiseVoterList
from ..serializers import VoteWiseVoterListSerializer


@api_view(['GET', 'POST'])
def voteWiseVoter_listCreate(request):
    """
    List all code voteWiseVoter, or create a new voteInfo.
    """
    if request.method == 'GET':
        voteWiseVoter = VoteWiseVoterList.objects.all()
        serializer = VoteWiseVoterListSerializer(voteWiseVoter, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VoteWiseVoterListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def voteWiseVoter_detail(request, id):
    """
    Retrieve, update or delete a code voteInfo.
    """
    try:
        voteInfo = VoteWiseVoterList.objects.get(id=id)
    except VoteWiseVoterList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VoteWiseVoterListSerializer(voteInfo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VoteWiseVoterListSerializer(voteInfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        voteInfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)