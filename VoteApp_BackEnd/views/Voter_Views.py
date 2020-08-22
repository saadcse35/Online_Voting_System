from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Voter
from ..serializers import VoterSerializer


@api_view(['GET', 'POST'])
def voter_listCreate(request):
    """
    List all code voters, or create a new voter.
    """
    if request.method == 'GET':
        voters = Voter.objects.all()
        serializer = VoterSerializer(voters, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VoterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def voter_detail(request, id):
    """
    Retrieve, update or delete a code voter.
    """
    try:
        voter = Voter.objects.get(id=id)
    except Voter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VoterSerializer(voter)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VoterSerializer(voter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        voter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)