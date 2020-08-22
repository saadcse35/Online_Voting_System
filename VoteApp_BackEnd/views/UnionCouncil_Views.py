from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import UnionCouncil
from ..serializers import UnionCouncilSerializer


@api_view(['GET', 'POST'])
def unionCouncil_listCreate(request):
    """
    List all code unionCouncils, or create a new unionCouncil.
    """
    if request.method == 'GET':
        unionCouncils = UnionCouncil.objects.all()
        serializer = UnionCouncilSerializer(unionCouncils, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UnionCouncilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def unionCouncil_detail(request, id):
    """
    Retrieve, update or delete a code unionCouncil.
    """
    try:
        unionCouncil = UnionCouncil.objects.get(id=id)
    except UnionCouncil.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UnionCouncilSerializer(unionCouncil)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UnionCouncilSerializer(unionCouncil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        unionCouncil.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)