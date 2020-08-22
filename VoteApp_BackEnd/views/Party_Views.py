from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Party
from ..serializers import PartySerializer


@api_view(['GET', 'POST'])
def party_listCreate(request):
    """
    List all code partys, or create a new party.
    """
    if request.method == 'GET':
        partys = Party.objects.all()
        serializer = PartySerializer(partys, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PartySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def party_detail(request, id):
    """
    Retrieve, update or delete a code party.
    """
    try:
        party = Party.objects.get(id=id)
    except Party.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PartySerializer(party)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PartySerializer(party, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        party.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)