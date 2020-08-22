from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import VoteCalculation
from ..serializers import VoteCalculationSerializer


@api_view(['GET', 'POST'])
def voteCalculation_listCreate(request):
    """
    List all code voteCalculation, or create a new voteInfo.
    """
    if request.method == 'GET':
        voteCalculation = VoteCalculation.objects.all()
        serializer = VoteCalculationSerializer(voteCalculation, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VoteCalculationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def voteCalculation_detail(request, id):
    """
    Retrieve, update or delete a code voteInfo.
    """
    try:
        voteInfo = VoteCalculation.objects.get(id=id)
    except VoteCalculation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VoteCalculationSerializer(voteInfo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VoteCalculationSerializer(voteInfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        voteInfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)